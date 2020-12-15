import time
tic = time.perf_counter()
infile = open("day13.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()
arrival = int(inList[0])
print(arrival)
buslist = inList[1].replace(',x','').split(',')
min = int(buslist[0]) - (arrival % int(buslist[0]))
first_bus = int(buslist[0])
for bus in buslist:
    bus = int(bus)
    if (bus - arrival % bus) < min:
        min = bus - arrival % bus
        first_bus = bus
        print(min,first_bus)
print(first_bus * min)
toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
