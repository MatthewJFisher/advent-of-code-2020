import time
tic = time.perf_counter()
infile = open("day8.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

instDict = {}
instInd = 0

# nopList = []
# jmpList = []

for line in inList:
    op,val=line.split()
    val = int(val)
    # if op == 'nop':
    #     nopList.append(val)
    # if op == 'jmp':
    #     jmpList.append(val)
    instDict[instInd]={'op':op,'val':val}
    instInd+=1

# print('length of instruction list: '+str(len(instDict)))
# print('nop values: ')
# nopList.sort()
# print(nopList)
# print('jmp values: ')
# jmpList.sort()
# print(jmpList)

def nop(index,accN,val):
    index+=1
    return(index,accN)
def acc(index,accN,val):
    index+=1
    accN+=val
    return(index,accN)
def jmp(index,accN,val):
    index+=val
    return(index,accN)

def execute_code(argument,index,accN,val):
    switcher = {
        'nop': (nop,[index,accN,val]),
        'acc': (acc,[index,accN,val]),
        'jmp': (jmp,[index,accN,val])
    }
    func, args = switcher[argument]
    # print('executing '+ argument + '('+str(index)+')')
    return(func(*args))

indDict = {}
i = 0
accN = 0
accOld = 0
counter = 0
indList = []
while i not in indDict:
    indDict[i]=1
    accOld = accN
    # print((instDict[i]['op'],instDict[i]['val']))
    if instDict[i]['op']!='acc' and instDict[i]['val']!=1 and (instDict[i]['op'],instDict[i]['val']!=('nop',0)):
        # counter +=1
        indList.append(i)
    i,accN = execute_code(instDict[i]['op'],i,accN,instDict[i]['val'])
    # print(accN)
else:
    print('final acc '+str(accOld))

# print('counter: '+str(counter))
# print(indList)

found = False

for index in indList:
    indDict = {}
    i = 0
    accN = 0
    accOld = 0
    while i not in indDict:
        indDict[i]=1
        accOld = accN
        # print((instDict[i]['op'],instDict[i]['val']))
        if i >= len(instDict):
            print('actual final acc '+str(accN))
            found = True
            break

        op = instDict[i]['op']
        val = instDict[i]['val']
        if i == index:
            if op=='nop':
                op = 'jmp'
            else:
                op = 'nop'

        i,accN = execute_code(op,i,accN,val)
        # print(accN)
    else:
        print('final acc '+str(accOld))
    if found:
        break
toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
