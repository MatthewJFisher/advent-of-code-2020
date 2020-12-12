import time
tic = time.perf_counter()
infile = open("day12.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

def interpret_op(op, current_dir_index):
    dirList = ['N','E','S','W']

    if op[0] == 'L':
        current_dir_index -=int(op[1:])/90
        if current_dir_index < 0:
            current_dir_index+=4
        if current_dir_index == 0:
            return(0,0,current_dir_index)
        elif current_dir_index == 1:
            return(0,0,current_dir_index)
        elif current_dir_index == 2:
            return(0,0,current_dir_index)
        elif current_dir_index == 3:
            return(0,0,current_dir_index)
    elif op[0] == 'R':
        current_dir_index +=int(op[1:])/90
        if current_dir_index > 3:
            current_dir_index-=4
        if current_dir_index == 0:
            return(0,0,current_dir_index)
        elif current_dir_index == 1:
            return(0,0,current_dir_index)
        elif current_dir_index == 2:
            return(0,0,current_dir_index)
        elif current_dir_index == 3:
            return(0,0,current_dir_index)
    elif op[0] == 'F':
        if current_dir_index == 0:
            return(0,int(op[1:]),current_dir_index)
        elif current_dir_index == 1:
            return(int(op[1:]),0,current_dir_index)
        elif current_dir_index == 2:
            return(0,-int(op[1:]),current_dir_index)
        elif current_dir_index == 3:
            return(-int(op[1:]),0,current_dir_index)

    elif op[0] == 'N':
        return(0,int(op[1:]),current_dir_index)
    elif op[0] == 'E':
        return(int(op[1:]),0,current_dir_index)
    elif op[0] == 'S':
        return(0,-int(op[1:]),current_dir_index)
    elif op[0] == 'W':
        return(-int(op[1:]),0,current_dir_index)

current_dir_index = 1 #starting East
x,y=0,0
for op in inList:
    dx,dy,current_dir_index=interpret_op(op,current_dir_index)
    x+=dx
    y+=dy

print(abs(x)+abs(y))

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
