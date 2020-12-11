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

def isValidField(label,data):
    if label == 'byr' and data.isdecimal() and int(data)>1919 and int(data)<2003:
        return True
    if label == 'iyr' and data.isdecimal() and int(data)>2009 and int(data)<2021:
        return True
    if label == 'eyr' and data.isdecimal() and int(data)>2019 and int(data)<2031:
        return True
    if label == 'hgt' and data.isalnum() and \
                        ((data[-2:]=='cm' and data[:-2].isdecimal() and \
                        int(data[:-2])>149 and int(data[:-2])<194) or \
                        (data[-2:]=='in' and data[:-2].isdecimal() and \
                        int(data[:-2])>58 and int(data[:-2])<77)):
        return True
    if label == 'hcl' and data[0]=='#' and len(data[1:])==6 and int(data[1:], 16) > 0:
        return True
    if label == 'ecl' and (data == 'amb' or data == 'blu' or data == 'brn' or \
                           data == 'gry' or data == 'grn' or data == 'hzl' or data == 'oth'):
        return True
    if label == 'pid' and len(data)==9 and data.isdecimal():
        return True
    if label == 'cid':
        return True
    return False

vDict = {}
vInd = 0

for pp in pDict:

    if p0 in pDict[pp] and \
       p1 in pDict[pp] and \
       p2 in pDict[pp] and \
       p3 in pDict[pp] and \
       p4 in pDict[pp] and \
       p5 in pDict[pp] and \
       p6 in pDict[pp]:
        vString = pDict[pp]
        invalidField = False
        for field in vString.split():

            label = field.split(':')[0]
            data = field.split(':')[1]
            if not isValidField(label,data):

                invalidField = True
                break
        if invalidField:
            continue
        else:
            valid += 1

print(valid)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
