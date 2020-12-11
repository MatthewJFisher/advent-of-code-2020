import time
tic = time.perf_counter()
infile = open("day3.in", "r")
inString = infile.read()
inList = inString.splitlines()

x0 = 0
y0 = 0
dx = 3
dy = 1

row_length = len(inList[0])

treeDict = {}
row_index = 0
for row in inList:
    char_index = 0
    treeDict[row_index] = {}
    for char in row:
        if char == '#':
            treeDict[row_index][char_index] = 1
        char_index +=1
    row_index +=1

def ride_toboggan(treeDict,x0,y0,dx,dy,row_length):
    x = x0 + dx
    y = y0 + dy
    treeSum = 0

    while y < len(treeDict):


        while x >= row_length:
            x -= row_length
        if x < 0:
            print('Error, x should not be negative!')
        if x in treeDict[y]:
            treeSum += 1
        x = x + dx
        y = y + dy

    return(treeSum)

result = ride_toboggan(treeDict,x0,y0,1,1,row_length) *\
         ride_toboggan(treeDict,x0,y0,3,1,row_length) *\
         ride_toboggan(treeDict,x0,y0,5,1,row_length) *\
         ride_toboggan(treeDict,x0,y0,7,1,row_length) *\
         ride_toboggan(treeDict,x0,y0,1,2,row_length)

print(result)


toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
