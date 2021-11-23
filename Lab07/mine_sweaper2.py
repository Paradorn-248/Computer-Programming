roww, coll = input("Grid Size: ").split()
row = int(coll)+2
col = int(roww)+2

m = int(input("Number of mine(s): "))
ar = [[0]*col for x in range(row)]
# print(ar)
for x in range(m):
    mrow, mcol = input("Mine#%d: " % (x+1)).split()
    mrow = int(mrow)+1
    mcol = int(mcol)+1
    ar[mcol][mrow] = 9

for x in range(1, row-1):
    for y in range(1, col-1):
        if ar[x][y] == 9:
            print("X", end=' ')
        else:
            cnt = int(0)
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    #print("%d %d"%(a,b))
                    if ar[a][b] == 9:
                        #print("%d %d"%(a,b))
                        cnt += 1
            print(cnt, end=' ')
    print()
