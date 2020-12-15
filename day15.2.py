import time
tic = time.perf_counter()
# infile = open("day15.in", "r")
infile = open("test.in", "r")

inString = infile.read()
inList = inString.strip().split(',')
inList = list(map(int, inList))


starting_turn = len(inList)+1
ledger = {}

def play_game(ledger = ledger, turns = 20, starting_list = inList):

    current_turn = 0
    num = 0
    while(current_turn<turns):
        if current_turn<len(inList):
            num = inList[current_turn]
        else:
            num = ledger['previous'][1]

        if num in ledger:
            ledger['previous']=(num,current_turn-ledger[num])
        else:
            ledger['previous']=(num,0)

        if ledger['previous'] in ledger:
            print('loop found')
        ledger[ledger['previous']]=current_turn
        ledger[num]=current_turn
        print(ledger['previous'])
        current_turn += 1
    return(num)

print(play_game())

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
