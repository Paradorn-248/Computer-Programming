n = int(input('Input n: '))
m = int(input('Input m: '))
ar = []
res = []
for i in range(n) :
    tmp = input().strip().split()
    ar.append(tmp)
# print(ar)
for num in range(1,m*n+1) :
    for i in range(n) :
        for j in range(m) :
            if ar[i][j] == str(num):
                res.append(f'({i},{j})')

for i in res :
    print(i)