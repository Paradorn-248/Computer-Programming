gold = float(input('Input Gold: '))
mod1 = gold // 1000

if gold < 1000 :
    print('Not enough gold.')
    exit()

def head(mod) :
    print(' ' + 'o' * (3*mod + 4))
    for _ in range(2*mod + 1) :
        print('o' * (3*mod + 6))
    print(' ' + 'o' * (3*mod + 4))

def holder(mod) :
    space = ' ' * (mod+3)
    stick = 'o' * mod
    for _ in range(mod+2) :
        print(space+stick)

def button(mod) :
    space = ' ' * (mod + 2)
    for _ in range(mod) :
        print(space + 'o'*(mod+2))
    print(space + ' ' + 'o' * mod)


mod = int(mod1)
head(mod)
holder(mod)
button(mod)