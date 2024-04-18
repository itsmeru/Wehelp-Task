import urllib.request as req
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

spot_url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
mrt_url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
with req.urlopen(mrt_url) as response:
    files=response.read().decode("utf-8")
    file=json.loads(files)
mrt_list=file["data"]

with req.urlopen(spot_url) as response:
    files=response.read().decode("utf-8")
    file=json.loads(files)
spot_list=file["data"]["results"]

mrt_dic={}
with open ("./week3/spot.csv","w",encoding="utf-8") as spot_file:
    for data in spot_list:
        img_src=data["filelist"].lower()
        distinct_place=None
        start_index = img_src.find("https:")
        end_index = img_src.find(".jpg") + 4
        first_url = img_src[start_index:end_index]

        for item in mrt_list:
            if item["SERIAL_NO"] == data["SERIAL_NO"]:
                distinct_place=item["address"][5:8]
                break
                
        spot_file.write("{},{},{},{},{}\n".format(data["stitle"],distinct_place,data["longitude"],data["latitude"],first_url))

        for item in mrt_list:
            if item["SERIAL_NO"] == data["SERIAL_NO"]:
                if item["MRT"] in mrt_dic:
                    mrt_dic[item["MRT"]].append(data["stitle"])
                else:
                    mrt_dic[item["MRT"]]=[data["stitle"]]
                break
    
with open ("./week3/mrt.csv","w",encoding="utf-8") as mrt_file:
    for mrt , place in mrt_dic.items():
        mrt_file.write("{},{}\n".format(mrt,",".join(place)))





