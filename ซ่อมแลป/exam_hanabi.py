def matZero(n):
    return [[0]*n for i in range(n)]

def firework1(m):
    res = matZero(m)
    for i in range(m):
        for j in range(m):
            if i==j or i==m//2 or j==m//2 or m-i-1==j: 
                res[i][j]=1
    return res
    
def firework2(n):
    m = n*2-1
    res = matZero(m)
    for i in range(m):
        for j in range(m):
            res[i][j]=n+1
    tmp = m+1
    k = -1
    while(tmp):
        tmp -= 1
        k += 1
        for i in range(k,tmp):
            for j in range(k,tmp):
                res[i][j] -= 1 
    return res
    
n = int(input('Sky : '))
sky = matZero(n)
h = int(input('Hanabi : '))

while(h):
    h -= 1
    s = input().split()
    for i in range(len(s)): 
        s[i]=int(s[i])
    r,c,t,m = s[0],s[1],s[2],s[3]

    if t==1: 
        ar=firework1(m)
        for i in range(r-m//2,r+m//2+1):
            for j in range(c-m//2,c+m//2+1):
                if i<0 or i>=n or j<0 or j>=n: 
                    continue
                sky[i][j]+=ar[i-(r-m//2)][j-(c-m//2)]
    if t==2: 
        ar=firework2(m)
        for i in range(r-m+1,r+m):
            for j in range(c-m+1,c+m):
                if i<0 or i>=n or j<0 or j>=n: 
                    continue
                sky[i][j]+=ar[i-(r-m+1)][j-(c-m+1)]

for i in range(n):
    for j in range(n):
        if sky[i][j]==0:
            ans='.'
        else :
            ans=sky[i][j]%10
        print(f'{ans}',end=' ')
    print()