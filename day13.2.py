import time
tic = time.perf_counter()
infile = open("day13.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()
buslist = inList[1].split(',')

a = []
n = []
N = 1

for i,bus in enumerate(buslist):
    if bus.isdecimal():
        a.append(int(bus) - i)
        n.append(int(bus))
        N = N * int(bus)

print(a)
print(n)
print(N)

def ChineseRemainderGauss(n,N,a):
    result = 0
    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = N // ni

        result += ai * bi * pow(bi,-1,ni)
    return result % N

print(ChineseRemainderGauss(n,N,a))


toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
