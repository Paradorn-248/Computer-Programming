def readlines() :
    with open("move.txt") as f :
        lines = [line.strip() for line in f]
    return lines

start = input('Initial position : ').split(',')
x = int(start[0])
y = int(start[1])
lines = readlines()
for i in lines :
    if i == 'L' :
        x -= 1
    elif i == 'R' :
        x += 1
    elif i == 'U' :
        y += 1
    elif i == 'D' :
        y -= 1
    else :
        print('invalid command')
        exit()
print(f'Robot stops at {x},{y}')