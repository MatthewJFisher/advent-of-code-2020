import time
tic = time.perf_counter()
infile = open("day1.in", "r")
inString = infile.read()
inList = inString.splitlines()
listLength = len(inList)
numList = list(map(int, inList))

found = False
for i in range(listLength):
    a = numList[i]
    twoSum = 2020 - a
    numDict = dict.fromkeys(numList[i+1:listLength], 1)
    for num in numDict:
        opp_num = twoSum - num
        if opp_num in numDict:
            print(num*opp_num*a)
            found = True
            break

    if found:
        break
toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.4f}")
