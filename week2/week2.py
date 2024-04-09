print("=== Task 1 ===")
def find_and_print(messages, current_station):
    if current_station=="Qizhang":
        print("Leslie")
        return
    greenLine=["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjing Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"]
    minNear=float("inf") 
    currentStationIndex=greenLine.index(current_station)
    for key,value in messages.items():
        for greenIndex,station in enumerate(greenLine):
            if station in value:
                if abs(greenIndex-currentStationIndex)<minNear:
                    minNear=abs(greenIndex-currentStationIndex)
                    friend=key
    print(friend)
messages={
"Leslie":"I'm at home near Xiaobitan station.",
 "Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.", 
"Copper":"I just saw a concert at Taipei Arena.",
 "Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian

print("=== Task 2 ===")
JohnSchedule = [0] * 24
BobSchedule = [0] * 24
JennySchedule = [0] * 24
def book(consultants, hour, duration, criteria):
    if criteria=="price":
        priortiy = sorted(consultants,key=lambda x:x[criteria])
    else:
        priortiy = sorted(consultants,key=lambda x:x[criteria],reverse=True)
    for check in priortiy:
        if check["name"] == "John" and 1 not in JohnSchedule[hour:hour + duration+1]:
            for i in range(hour, hour + duration+1):
                JohnSchedule[i] = 1
            print(check["name"])
            return
        elif check["name"] == "Bob" and 1 not in BobSchedule[hour:hour + duration+1]:
            for i in range(hour, hour + duration+1):
                BobSchedule[i] = 1
            print(check["name"])
            return
        elif check["name"] == "Jenny" and 1 not in JennySchedule[hour:hour + duration+1]:
            for i in range(hour, hour + duration+1):
                JennySchedule[i] = 1
            print(check["name"])
            return
    print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000},
 {"name":"Bob", "rate":3, "price":1200}, 
 {"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service 
book(consultants, 14, 3, "price") # John 

print("=== Task 3 ===")
def func(*data):
    middles={}
    flag=0
    for name in data:
        middle=name[len(name)//2]
        if middle in middles:
            middles[middle].append(name)
        else:
            middles[middle] = [name]
    for names in middles.values():
        if len(names)==1:
            print("".join(names))
            flag=1
            break
    if flag==0:
        print("沒有")
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("=== Task 4 ===")
def get_number(index):
    sum=0
    for i in range(index):
        if (i+1)%3==0:
            sum-=1
        else:
            sum+=4
    print(sum)
get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70

print("=== Task 5 ===")
def find(spaces, stat, n):
    minNum=float("inf")
    index=-1
    for i,num in enumerate(spaces):
        if stat[i]==1 and num>=n:
            if num-n <minNum:
                minNum=num-n
                index=i
    print(index)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
