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

for line in inList:
    if line == "":
        uString=""
        for char in gDict[gInd]:
            if char not in uString:
                uString+=char
        print(uString)
        uSum+=len(uString)
        gInd += 1
        gDict[gInd]=""
        continue
    gDict[gInd]+=line.strip()
else:
    uString=""
    for char in gDict[gInd]:
        if char not in uString:
            uString+=char
    print(uString)
    uSum+=len(uString)
print(uSum)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
