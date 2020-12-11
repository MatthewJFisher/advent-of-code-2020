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
    conDict[container]={}
    if 'no other' in contained:
        conDict[container]=False
        continue
    if ',' not in contained:
        num = ''
        for char in contained:
            if char.isdecimal():
                num += char
                contained = contained.replace(char,'')
        contained = contained.strip()
        conDict[container][contained]=int(num)

    else:
        conList = contained.split(',')
        for bag in conList:
            num = ''
            for char in bag:
                if char.isdecimal():
                    num += char
                    bag = bag.replace(char,'')
            bag = bag.strip()
            conDict[container][bag]=int(num)

print(conDict)

target = 'shiny gold'

def count_bags(conDict,target,starting_sum = 0):
    sum = starting_sum
    if target in conDict and conDict[target]:
        for bag in conDict[target]:
            nBags = conDict[target][bag]
            sum += nBags
            sum += nBags * count_bags(conDict,bag)

    return(sum)

result = count_bags(conDict,target)

print("result= "+str(result))

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
