import time
tic = time.perf_counter()
infile = open("day14.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

mem = {}
mask = ''

def set_bit(value, bit_index):
    return value | (1 << bit_index)
def toggle_bit(value, bit_index):
    return value ^ (1 << bit_index)

maskList = []
newmask = ''
for line in inList:
    address = -1
    operation,value = line.split('=')[0].strip(),line.split('=')[1].strip()
    if operation == 'mask':
        maskList = []
        mask = value
        nX = 0
        Xindices = []
        newmask = ''
        for i,char in enumerate(mask):
            if char == 'X':
                nX += 1
                Xindices.append(i)
                newmask += '0'
            else:
                newmask += char
        nXMasks = pow(2,nX)
        maskList = [0]*nXMasks
        print(Xindices)
        for i,XMask in enumerate(maskList):
            bin_i = bin(i)[2:]
            bin_i = (nX - len(bin_i))*'0'+bin_i
            print(bin_i)
            for j,char in enumerate(bin_i):
                if char == '0':
                    continue
                else:
                    XMask = set_bit(XMask,35 - Xindices[j])
            print('XMask: ' + bin(XMask))
            maskList[i]=XMask

    else:
        value = int(value)
        address = int(operation.split('[')[1].rstrip(']'))
        masked_address = address | int(newmask,2)
        addresses = []
        for XMask in maskList:
            # print(address^XMask)
            print(bin(masked_address))
            print(bin(XMask))
            print('address: ' + str(masked_address^XMask))
            print('value: ' + str(value) )
            mem[masked_address^XMask]=value
mem_sum = 0

print(mem)
for address in mem:
    mem_sum += mem[address]

print(mem_sum)

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
