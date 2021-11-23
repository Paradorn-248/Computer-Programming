def map_get(size) :
    res = []
    size[0],size[1] = int(size[0]),int(size[1])
    for _ in range(size[0]) :
        n = input().split()
        for j in range(size[1]) :
            n[j] = int(n[j])
        res.append(n)
    # print(res)
    return res

def north(size,map) :
    res = 0
    row,column = size[0],size[1]
    for i in range(column) :
        max = map[0][i]
        for j in range(row) :
            if max < map[j][i] :
                res += 1
                max = map[j][i]
            else :
                continue
    return res + column

def south(size,map) :
    res = 0
    row,column = size[0],size[1]
    for i in range(column) :
        max = map[row-1][i]
        for j in range(row-1,-1,-1) :
            if max < map[j][i] :
                res += 1
                max = map[j][i]
            else :
                continue
    return res + column

def west(size,map) :
    res = 0
    row,column = size[0],size[1]
    for i in range(row) :
        max = map[i][0]
        for j in range(column) :
            if max < map[i][j] :
                res += 1
                max = map[i][j]
            else :
                continue
    return res + row
    
def east(size,map) :
    res = 0
    row,column = size[0],size[1]
    for i in range(row) :
        max = map[i][column-1]
        for j in range(column-1,-1,-1) :
            if max < map[i][j] :
                res += 1
                max = map[i][j]
            else :
                continue
    return res + row

size = input('City Size: ').split()
# size = [4,5]
map = map_get(size)
# map = [[2, 3, 5, 6, 2], [1, 3, 4, 7, 1], [6, 5, 4, 1, 3], [2, 3, 7, 9, 6]]
# print(north(size,map))
# print(south(size,map))
# print(west(size,map))
# print(east(size,map))
# print(map)

N = north(size,map)
S = south(size,map)
E = east(size,map)
W = west(size,map)
arrans = list('NSEW')
arr= [N,S,E,W]
max_view = max(arr)
# print(max_view)
# print(arr)
for i in range(4) :
    if arr[i] == max_view :
        print(arrans[i],end = ' ')

