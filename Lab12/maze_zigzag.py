n = int(input())
listt = [[] for i in range(n)]
# print(listt)
a = 1
c = 1

if n == 1 :
    print(f'{1:3.0f}',end=' ')    
else :
    while True :
        if c %2 != 0 :
            for i in range(c) :
                listt[n-i-1].append(a)
                a += 1
            c += 1
        else :
            for i in range(c-1,-1,-1) :
                listt[n-i-1].append(a)
                a += 1
            c += 1
        if c == n+1 :
            break

    c = n - 1

    while True :
        if c %2 == 0 :
            for i in range(c) :
                listt[i].append(a)
                a += 1
            c -= 1
        else :
            for i in range(c-1,-1,-1) :
                listt[i].append(a)
                a += 1
            c -= 1
        if c == 0 :
            break

for i in range(len(listt)):
    for j in range(len(listt[0])):
        print(f'{listt[i][j]:3.0f}',end=' ')
    print()