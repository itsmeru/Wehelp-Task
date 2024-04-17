import urllib.request as req
import ssl
import bs4
import threading
ssl._create_default_https_context = ssl._create_unverified_context

def urlRequest(url):
    request=req.Request(url,headers={
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "cookie":"over18=1"
            })
    return request

def get_page_data(page_url):
    request = urlRequest(page_url)
    with req.urlopen(request) as page_file:
        data = page_file.read().decode("utf-8")
    page_root = bs4.BeautifulSoup(data, "html.parser")
    meta_value_elements = page_root.find_all(class_="article-meta-tag")    
    time = None
    if meta_value_elements:
        for element in meta_value_elements:
            if "時間" in element.text:
                time_element = element.find_next_sibling(class_="article-meta-value")
                if time_element:
                    time = time_element.text.strip() 
                else:
                    time=""
    return time

def process_page_data(page_url ,title ,like_count,result):
    time  = get_page_data(page_url)
    result.append((title, like_count,time))

def get_data(lot_url):
    request=urlRequest(lot_url)
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    lot_root = bs4.BeautifulSoup(data,"html.parser")
    titles = lot_root.find_all("div",class_="title")
    push_tag = lot_root.find_all(class_="hl f2")

    data_list = []
    for title, like in zip(titles,push_tag):
        if title.a is not None:
            page = "https://www.ptt.cc" + title.a.get("href")
            like_count = like.text if like else 0 
            data_list.append((title.a.string,like_count,page))
    threads = []
    result = []
    for title,like_count ,page_url in data_list:
        thread = threading.Thread(target=process_page_data, args=(page_url,title,like_count,result))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    for title, like_count ,time in result:
        file.write("{},{},{}\n".format(title, like_count,time))
    nextpage = lot_root.find("a",string="‹ 上頁")
    return nextpage["href"]



with open("./week3/article.csv", "w", encoding="utf-8") as file:
    lot_url="https://www.ptt.cc/bbs/Lottery/index.html"
    count=0
    while count<3:
        lot_url="https://www.ptt.cc"+get_data(lot_url)
        count+=1