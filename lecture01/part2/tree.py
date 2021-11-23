h = int(input('h: '))
char = input('Character: ')
invert = input('Is the tree invert?(y/n): ')

if invert == 'n' :
    for i in range(h) :
        space = ' ' * (h - i-1)
        print(space + ((char) * (2*i + 1)))

    for i in range(h//2) :
        space = ' ' * (h - 1)
        print(space + char)

if invert == 'y' :
    for i in range(h//2) :
        space = ' ' * (h-1)
        print(space + char)
        
    for i in range(h) :
        space = ' ' * i
        print(space + ((char) * ((2*h)-1)))   
        h -= 1  
