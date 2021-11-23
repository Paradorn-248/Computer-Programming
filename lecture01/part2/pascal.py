def fac(n) :
    res = 1
    for i in range(1,n+1) :
        res *= i
    return res

def select(n,r) :
    res = fac(n)//(fac(n-r)*fac(r))
    return res


n = int(input('Input: '))

for i in range(n) :
    for r in range(i+1) :
        print(select(i,r),end=' ')
    print()
