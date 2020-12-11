import time
tic = time.perf_counter()
infile = open("day2.in", "r")
inString = infile.read()
inList = inString.splitlines()

valid = 0

for entry in inList:
    entryList = entry.split(':')
    rule = entryList[0].strip()
    pwd = entryList[1].strip()
    rChar = rule.split()[1]
    r0 = int(rule.split()[0].split("-")[0].strip())-1
    r1 = int(rule.split()[0].split("-")[1].strip())-1
    if (pwd[r0]==rChar)!=(pwd[r1]==rChar):
        valid +=1

print(valid)
toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.4f}")
