row,col = input("Grid Size: ").split()
row = int(row) + 2
col = int(col) + 2
ar = [[0]*row for i in range(col)]
mine = int(input('Number of mine(s): '))

for i in range(mine) :
    rget,cget = input(f'Mine#{i+1}: ').split()
    rget = int(rget)+1
    cget = int(cget)+1
    ar[cget][rget] = 'X'

for i in range(1,col-1) :
    for j in range(1,row-1) :
        if ar[i][j] != 'X' :
            for a in range(i-1,i+2) :
                for b in range(j-1,j+2) :
                    if ar[a][b] == 'X' :
                        ar[i][j] += 1

for i in range(1,col-1) :
    for j in range(1,row-1) :
        print(ar[i][j],end=' ')
    print()
# print(ar)