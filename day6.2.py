import time
tic = time.perf_counter()
infile = open("day6.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

gDict = {}

gInd=0

gDict[0]=""

uSum=0

gNum=0

for line in inList:
    if line == "":
        uString=""
        for char in gDict[gInd]:
            if (char not in uString) and gDict[gInd].count(char)==gNum:
                uString+=char
        # print(uString)
        uSum+=len(uString)
        gNum=0
        gInd += 1
        gDict[gInd]=""
        continue
    gNum+=1
    gDict[gInd]+=line.strip()
else:
    uString=""
    for char in gDict[gInd]:
        if (char not in uString) and gDict[gInd].count(char)==gNum:
            uString+=char
    # print(uString)
    uSum+=len(uString)
print(uSum)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
