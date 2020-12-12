import time
tic = time.perf_counter()
infile = open("day11.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()


y = 0
seatDict = {}
for line in inList:
    x = 0
    for char in line:
        if char == 'L' or char == '#':
            seatDict[(x,y)]=1
        x += 1
    y += 1

def apply_rule(seatDict_in):
    seatDict_out = {}
    nSeats = len(seatDict_in)
    nUnchanged = 0
    stable = False
    for seat in seatDict_in:
        x,y = seat
        occ_n = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if (i,j)==(x,y):
                    continue
                if (i,j) in seatDict_in:
                    if seatDict_in[(i,j)]:
                        occ_n+=1
        if seatDict_in[seat] and occ_n > 3:
            seatDict_out[seat]=0
        elif not seatDict_in[seat] and occ_n == 0:
            seatDict_out[seat]=1
        else:
            nUnchanged += 1
            seatDict_out[seat]=seatDict_in[seat]
    if nUnchanged == nSeats:
        stable = True
    return(seatDict_out,stable)

stable = False
occupied = 0
while not stable:
    seatDict,stable = apply_rule(seatDict)
else:
    for seat in seatDict:
        occupied += seatDict[seat]

print(occupied)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
