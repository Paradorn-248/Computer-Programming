def print_table(row,column,table) :
    for i in range(row) :
        for j in range(column) :
            print(table[i][j],end =' ')
        print()


grid_size = input('Grid Size: ').split()
column = int(grid_size[0])
row = int(grid_size[1])
table = [[0]*column for i in range(row)]
amount = int(input('Number of mine(s): '))
for i in range(amount) :
    get = input(f'Mine#{i+1}: ').split()
    coor1,coor2 = int(get[0]),int(get[1])
    table[coor2][coor1] = 'X'
# print(table)
nub_bomb = 0
for i in range(row) :
    for j in range(column) :
        if table[i][j] != 'X' :
            if i == 0 or i == row-1 or j == 0 or j == column - 1 :
                if i == 0 and j == 0 :
                    if table[i+1][j] == 'X' :
                        nub_bomb += 1
                    if table[i][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j+1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif i == 0 and j == column - 1 :
                    if table[i+1][j] == 'X' :
                        nub_bomb += 1
                    if table[i][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j-1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif i == row-1 and j == 0 :
                    if table[i][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j+1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif i == row-1 and j == column - 1 :
                    if table[i][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j-1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif i == 0 :
                    if table[i][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j+1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif i == row - 1 :
                    if table[i][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j+1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif j == 0 :
                    if table[i-1][j] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j] == 'X' :
                        nub_bomb += 1
                    if table[i][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j+1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j+1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb

                elif j == column -1 :
                    if table[i-1][j] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j] == 'X' :
                        nub_bomb += 1
                    if table[i][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i-1][j-1] == 'X' :
                        nub_bomb += 1
                    if table[i+1][j-1] == 'X' :
                        nub_bomb += 1
                    table[i][j] = nub_bomb
                nub_bomb = 0

            else :
                if table[i-1][j-1] == 'X'  :
                    nub_bomb += 1
                if table[i-1][j] == 'X' :
                    nub_bomb += 1
                if table[i-1][j+1] == 'X'  :
                    nub_bomb += 1
                if table[i][j-1] == 'X'  :
                    nub_bomb += 1
                if table[i][j+1] == 'X'  :
                    nub_bomb += 1
                if table[i+1][j-1] == 'X'  :
                    nub_bomb += 1
                if table[i+1][j] == 'X'  :
                    nub_bomb += 1
                if table[i+1][j+1] == 'X'  :
                    nub_bomb += 1
                table[i][j] = nub_bomb
            nub_bomb = 0

print_table(row,column,table)
