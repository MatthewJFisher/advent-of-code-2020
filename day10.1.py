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
oldAdapter = 0

for adapter in inList:

    if adapter-oldAdapter == 1:
        num1+=1
    elif adapter-oldAdapter == 3:
        num3+=1
    elif adapter-oldAdapter > 3:
        print('Error, joltage difference too high')
        break
    elif adapter == oldAdapter:
        print('Error, joltage difference ZERO')

    oldAdapter = adapter

num3 += 1
print(num1*num3)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
