def upper(n) :
    m = n
    spacecount = 0
    for i in range(n) :
        space = ' ' * spacecount
        print(space, end ='')
        print('=' * (5 + 2*(m-1)))
        print(space, end ='')
        print(f"={'#'* (3+ (2*(m-1)))}=")
        m -= 1
        spacecount += 1

def lower(n) :
    m = 1
    spacecount = n
    for i in range(n//2) :
        space = ' ' * spacecount
        print(space, end ='')
        print(f"={'#' * m}= ")
        print(space, end ='')
        if i != n // 2 -1 :
            print('=' * (2*i + 3))
        m += 2
        spacecount -= 1


n = int(input('n: '))
upper(n)
print(f"{' ' * (n+1)}=")
lower(n)
