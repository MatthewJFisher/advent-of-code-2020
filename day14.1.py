import time
tic = time.perf_counter()
infile = open("day14.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

mem = {}
mask = ''
for line in inList:
    address = -1
    operation,value = line.split('=')[0].strip(),line.split('=')[1].strip()
    if operation == 'mask':
        mask = value
    else:
        address = int(operation.split('[')[1].rstrip(']'))
        value = bin(int(value))[2:]
        pad = 36 - len(value)
        value = pad*'0'+value
        masked_value = value
        for i,char in enumerate(mask):
            if char == 'X':
                continue
            else:
                masked_value = list(masked_value)
                masked_value[i]=char
                masked_value = ''.join(masked_value)
        mem[address]=int(masked_value, 2)

mem_sum = 0

for address in mem:
    mem_sum += mem[address]

print(mem_sum)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
