import time
tic = time.perf_counter()
infile = open("day8.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

instDict = {}
instInd = 0

for line in inList:
    op,val=line.split()
    val = int(val)
    instDict[instInd]={'op':op,'val':val}
    instInd+=1


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
while i not in indDict:
    indDict[i]=1
    accOld = accN
    # print((instDict[i]['op'],instDict[i]['val']))
    i,accN = execute_code(instDict[i]['op'],i,accN,instDict[i]['val'])
    # print(accN)
else:
    print('final acc '+str(accOld))

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
