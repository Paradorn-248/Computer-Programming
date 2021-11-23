def printmat(ar) :
    for i in range(len(ar)) :
        for j in range(len(ar)) :
            print(ar[i][j],end=' ')
        print()

def harn(n,c) :
    res = 0
    if n % c >0 :
        res = n//c+1
    else :
        res = n//c
    return res

n = int(input("Input the maze's size (only 1 to 9): "))
t = int(input('Input the type of maze (only 1 to 2): '))
# n = 7
# t = 2
tmp = 0
ar = []
for i in range(2*n-1) :
    tmp1 = []
    for j in range(2*n-1) :
        tmp1.append(0)
    ar.append(tmp1)

if t == 1 :
    nub = 1
    for i in range(harn(n,2)) : 
        for a in range(tmp,2*n-1-tmp) :
            for b in range(tmp,2*n-1-tmp) :
                ar[a][b] = nub
        nub += 2
        tmp += 1
    nub = 2
    for i in range(n-(harn(n,2))) : 
        for a in range(tmp,2*n-1-tmp) :
            for b in range(tmp,2*n-1-tmp) :
                ar[a][b] = nub
        nub += 2
        tmp += 1

if t == 2 :
    nub = 2
    for i in range(n//2) : 
        for a in range(tmp,2*n-1-tmp) :
            for b in range(tmp,2*n-1-tmp) :
                ar[a][b] = nub
        nub += 2
        tmp += 1
    nub = 1
    for i in range(n-(n//2)) : 
        for a in range(tmp,2*n-1-tmp) :
            for b in range(tmp,2*n-1-tmp) :
                ar[a][b] = nub
        nub += 2
        tmp += 1

printmat(ar)