import time
tic = time.perf_counter()
infile = open("day12.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

def rotate(deg, x, y):
    rot = int(deg/90)
    # print(rot)
    direction = int(deg/abs(deg))
    for i in range(abs(rot)):
        # print(i)
        # print(x,y,direction)
        x,y = (y*direction,-x*direction)
    return(x,y)
def translate(direction, magnitude, x, y):
    if direction == 'N':
        y += magnitude
    elif direction == 'S':
        y -= magnitude
    elif direction == 'E':
        x += magnitude
    elif direction == 'W':
        x -= magnitude
    return(x,y)
def move_ship(mult,sx,sy,wx,wy):
    sx += wx * mult
    sy += wy * mult
    return(sx,sy)

def interpret_op(op,sx,sy,wx,wy):
    # print('Start interpret')
    if op[0]=='R':
        # print('R')
        wx,wy=rotate(int(op[1:]),wx,wy)
        return(sx,sy,wx,wy)
    elif op[0]=='L':
        # print('L')
        wx,wy=rotate(-int(op[1:]),wx,wy)
        return(sx,sy,wx,wy)
    elif op[0]=='N' or op[0]=='E' or op[0]=='S' or op[0]=='W':
        wx,wy=translate(op[0],int(op[1:]),wx,wy)
        return(sx,sy,wx,wy)
    elif op[0]=='F':
        sx,sy=move_ship(int(op[1:]),sx,sy,wx,wy)

        return(sx,sy,wx,wy)
    else:
        print('ERROR, unexpected op')


sx = 0
sy = 0
wx = 10
wy = 1

for op in inList:
    sx,sy,wx,wy=interpret_op(op,sx,sy,wx,wy)
    # print(sx,sy,wx,wy)

print(abs(sx)+abs(sy))

toc = time.perf_counter()
print(f"time elapsed: {toc-tic:0.5f}")
