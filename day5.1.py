import time
tic = time.perf_counter()
infile = open("day5.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inString = inString.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
inList = inString.splitlines()

maxID = 0

for seat in inList:

    ID = int(seat,2)
    if ID > maxID:
        maxID = ID

print(maxID)
toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
