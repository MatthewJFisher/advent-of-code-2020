import time
tic = time.perf_counter()
infile = open("day9.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

inList = list(map(int, inList))

length = len(inList)
print(length)
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
        target = inList[i]
        break

print(target)

result = 0
# running_sum = inList[0]+inList[1]
# startInd = 0
# endInd = startInd + 1
# counter = 0
# while startInd<endInd and endInd<length:
#     counter +=1
#     if running_sum == target:
#         result = min(inList[startInd:endInd+1])+max(inList[startInd:endInd+1])
#         break
#     elif running_sum < target:
#         endInd+=1
#         running_sum += inList[endInd]
#     elif running_sum > target:
#         running_sum -= inList[startInd]
#         startInd+=1
# print(counter)
# print(result)
for i in range(length):
    running_sum = inList[i]
    if running_sum > target:
        continue
    for j in range(i+1,length):
        running_sum+=inList[j]

        if running_sum > target:
            break
        # print(running_sum)

        if running_sum==target:
            running_list = inList[i:j+1]
            result = max(running_list)+min(running_list)
            print(result)
            break


    if result:
        break

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
