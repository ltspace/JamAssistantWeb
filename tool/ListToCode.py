# 使用readline()读文件
f = open("hi.txt",encoding='utf-8')
ff = open("h.txt",encoding='utf-8')
while True:
    line = f.readline()
    date = ff.readline()
    if line:
        print ("<option value=\"",end="")
        line=line.strip('\n')
        date=date.strip('\n')
        print(date[0:4]+line,end="")
        print("\">\n",end="")
        print(line,end="")
        print("（",end="")
        print(date,end="")
        print("）\n</option>\n",end="")
    else:
        break
f.close()

