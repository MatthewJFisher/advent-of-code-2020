import time
tic = time.perf_counter()
infile = open("day10.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

inList = list(map(int, inList))
inList.sort()

num1 = 0
num3 = 0
num2 = 0
oldAdapter = 0
diffList = []
finalAdapter = inList[-1]+3

for adapter in inList:

    if adapter-oldAdapter == 1:
        num1+=1
    elif adapter-oldAdapter == 3:
        num3+=1
    elif adapter-oldAdapter == 2:
        num2+=1
    elif adapter-oldAdapter > 3:
        print('Error, joltage difference too high')
        break
    elif adapter == oldAdapter:
        print('Error, joltage difference ZERO')
    diffList.append(adapter-oldAdapter)
    oldAdapter = adapter

diffList.append(3)
num3 += 1
# print(num1*num3)
print('num1 = '+str(num1))
print('num2 = '+str(num2))
print('num3 = '+str(num3))

result = 1
prevDiff = 3
gapSum = 1
oldgapSum0 = 0
oldgapSum1 = 0
for diff in diffList:
    if diff == 3 and prevDiff != 3:
        print(gapSum)
        result *= gapSum
        prevDiff = diff
        gapSum = 1
        oldgapSum0 = 0
        oldgapSum1 = 0
        continue
    elif diff == 3 and prevDiff == 3:
        prevDiff = diff
        continue
    else:
        tempgapSum = gapSum
        gapSum += oldgapSum1 + oldgapSum0
        oldgapSum1 = oldgapSum0
        oldgapSum0 = tempgapSum
        prevDiff = diff
        continue


# print(diffList)
print(result)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
