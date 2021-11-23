n = int(input('n: '))
# n = 11
def upper(n) :
    star = '+'
    space = ' '
    for j in range(n//2) :
        res = ''
        res += space*(j) + star +space*((n//2)-1-j) + star +space*((n//2)-1-j) + star
        print(res)

def lower(n) :
    star = '+'
    space = ' '
    for j in range(n//2) :
        res = ''
        res += space*((n//2)-1-j) + star +space*(j) + star +space*(j) + star
        print(res)


upper(n)
print('+'*n)
lower(n)