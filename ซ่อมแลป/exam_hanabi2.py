def add():
    s = int(input("Sky : "))
    h = int(input("Hanabi : "))
    H = []
    for i in range(h) :
        r = input().strip().split() 
        for j in range(len(r)) :
            r[j] = int(r[j])
        H.append(r)
    return s,h,H

def hanabi1(n):
    res = [[' ' for i in range(n)] for j in range(n)]
    i,j = 0,0
    for a in range(n):
        res[i][j] = '1'
        i += 1
        j += 1
    i = 0
    j = int((n-1)/2)
    for a in range(n):
        res[i][j] = '1'
        i += 1
    i = int((n-1)/2)
    j = 0
    for a in range(n):
        res[i][j] = '1'
        j += 1
    i = 0
    j = n-1
    for a in range(n):
        res[i][j] = '1'
        i += 1
        j -=1
    return res

def hanabi2(n):
    res = [[0 for i in range(2*n-1)] for j in range(2*n-1)]
    i = 0
    j = 0
    x = n
    for _ in range(n):
        for a in range(i,len(res)-i):
            for b in range(j,len(res[0])-j):
                res[a][b] = x
        x -= 1
        i += 1
        j += 1
    return res

def show(s,pos):
    res = [['.' for i in range(s)] for j in range(s)]
    for i in pos:
        x,y = i[0],i[1]
        if i[2] == 2:
            h = hanabi2(i[3])
            for a in range(len(h)):
                for b in range(len(h[0])):
                    if x-i[3]+1+a < 0 or x-i[3]+1+a > s or y-i[3]+1+b < 0 or y-i[3]+1+b > s:
                        continue
                    if res[x-i[3]+1+a][y-i[3]+1+b] == '.':
                        res[x-i[3]+1+a][y-i[3]+1+b] = h[a][b]
                    else:
                        res[x-i[3]+1+a][y-i[3]+1+b] = (int(res[x-i[3]+1+a][y-i[3]+1+b])+int(h[a][b]))%10
        if i[2] == 1:
            c = int((i[3]-1)/2)
            h = hanabi1(i[3])
            for a in range(len(h)):
                for b in range(len(h[0])):
                    if h[a][b] == ' ':
                        continue
                    if x-c+a < 0 or x-c+a > s or y-c+b < 0 or y-c+b > s:
                        continue
                    if res[x-c+a][y-c+b] == '.':
                        res[x-c+a][y-c+b] = h[a][b] 
                    else:
                        res[x-c+a][y-c+b] = (int(res[x-c+a][y-c+b])+int(h[a][b]))%10
    for i in res:
        for j in i:
            print(j, end = ' ')
        print()

s,h,H = add()
# print(s)
# print(H)
show(s,H)