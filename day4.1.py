import time
tic = time.perf_counter()
infile = open("day4.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

pDict = {}

pInd = 0

pDict[0]=""

for line in inList:
    if line == "":
        pDict[pInd].strip()
        pInd += 1
        pDict[pInd]=""
        continue
    pDict[pInd]+=line.strip()
    pDict[pInd]+=" "

p0 = 'byr:'
p1 = 'iyr:'
p2 = 'eyr:'
p3 = 'hgt:'
p4 = 'hcl:'
p5 = 'ecl:'
p6 = 'pid:'
p7 = 'cid:'

valid = 0

# print(pDict)

for pp in pDict:
    if p0 in pDict[pp] and \
       p1 in pDict[pp] and \
       p2 in pDict[pp] and \
       p3 in pDict[pp] and \
       p4 in pDict[pp] and \
       p5 in pDict[pp] and \
       p6 in pDict[pp]:
       valid += 1

print(valid)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
