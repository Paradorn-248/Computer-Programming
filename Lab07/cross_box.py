N = int(input())

def box(n) :
    print('.'*n)
    for i in range((n-3)//2) :
        res = '.'
        dot = '.'
        space = ' '
        between_space = n-4
        res += space*i+dot+space*(between_space-(i*2))+dot+space*i+dot
        print(res)

    print('.'+' '*((n-3)//2)+'.'+' '*((n-3)//2)+'.')
    
    between_space = 1
    j = (n-3)//2 - 1
    for i in range((n-3)//2) :
        res = '.'
        dot = '.'
        space = ' '
        res += space*j + dot + space*between_space + dot + space*j + dot
        j -= 1
        between_space += 2
        print(res)

    print('.'*n)



box(N)
