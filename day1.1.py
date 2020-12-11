infile = open("day1.in", "r")
inString = infile.read()
inList = inString.splitlines()

listLength = len(inList)

for num in inList:
    num = int(num)
    opp_num = 2020 - num
    if inList.count(str(opp_num)):
        print(num*opp_num)
    else:
        inList.remove(str(num))
