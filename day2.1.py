infile = open("day2.in", "r")
inString = infile.read()
inList = inString.splitlines()

valid = 0

for entry in inList:
    entryList = entry.split(':')
    rule = entryList[0].strip()
    pwd = entryList[1].strip()
    rChar = rule.split()[1]
    rMin = int(rule.split()[0].split("-")[0].strip())
    rMax = int(rule.split()[0].split("-")[1].strip())
    if pwd.count(rChar)>=rMin and pwd.count(rChar)<=rMax:
        valid += 1

print(valid)
