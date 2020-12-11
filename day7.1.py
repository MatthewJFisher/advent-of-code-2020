import time
tic = time.perf_counter()
infile = open("day7.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inString = inString.replace('bags','').replace('bag','').replace('.','')
inList = inString.splitlines()

conDict = {}

for line in inList:
    container = line.split('contain')[0]
    contained = line.split('contain')[1]
    container = container.strip()
    if 'no other' in contained:
        continue
    if ',' not in contained:
        for char in contained:
            if char.isdecimal():
                contained = contained.replace(char,'')
        contained = contained.strip()
        if contained not in conDict:
            conDict[contained]=[container]
        else:
            conDict[contained].append(container)
    else:
        conList = contained.split(',')
        for bag in conList:
            for char in bag:
                if char.isdecimal():
                    bag = bag.replace(char,'')
            bag = bag.strip()
            if bag not in conDict:
                conDict[bag]=[container]
            else:
                conDict[bag].append(container)

targetDict = {}
target = 'shiny gold'

def count_bags(conDict,targetDict,target):
    if target in conDict:
        for bag in conDict[target]:
            if bag in targetDict:
                continue
            else:
                targetDict[bag]=1
                count_bags(conDict,targetDict,bag)
    else:
        if target not in targetDict:
            targetDict[bag]=1
            
count_bags(conDict,targetDict,target)
print(len(targetDict))


toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
