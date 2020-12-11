import time
tic = time.perf_counter()
infile = open("day5.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inString = inString.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
inList = inString.splitlines()

maxID = 0

seatDict = {}

for seat in inList:
    row = int(seat[:7],2)
    ID = int(seat, 2)
    seatDict[ID] = row
    if ID > maxID:
        maxID = ID

missingList = []

for i in range(maxID):
    if i not in seatDict:
        missingList.append(i)
print(missingList)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
