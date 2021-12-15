re = open("adat.txt", "r")
line = re.readline()
while line !="":
    line = line.strip()
    datas = line.split()
    print("%s/%s %s %s/%s =" % \
        (datas[0], datas[1],
         datas[4], datas[2],
         datas[3]))
    line = re.readline()
re.close()