import time
tic = time.perf_counter()
infile = open("day9.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

inList = list(map(int, inList))

length = len(inList)
pre = 25

target = 0
for i in range(pre,length):
    match = False
    preDict = {}
    preDict = preDict.fromkeys(inList[i-pre:i])

    for j in preDict:
        num = inList[i]
        if num - j in preDict and num - j != j:
            match = True
    if match == False:
        print(inList[i])
        target = inList[i]
        break




toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
