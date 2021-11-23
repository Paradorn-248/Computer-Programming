def readMinisodoku(filename) :
    with open(filename) as f :
        s = [line.strip().split(',') for line in f]
        print(s)
        # sodoku = []
        # i =0
        # while i < len(s) :
        #     add = []
        #     for j in range(int(len(s)**(1/2))) :
        #         add.append(s[i])
        #         i += 1
        #     sodoku.append(add)
        # print(sodoku)
    return s

def printMiniSodoku(a) :
    res = ''
    n = len(a)
    for i in range(n) :
        for j in range(n) :
            res += f"{a[i][j]:3}"
        if i < n - 1 :
            res += '\n'
    print(res)

def checkMiniSodoku(s) :
    j,k,nub = 0,0,0
    checkround = 0
    n = len(s)
    for i in range(n) :
        check_list = []
        for j in range(n) :
            nub = 0
            while nub != 3 and checkround <= n:
                check_list.append(s[i][j][k])
                k += 1
        checkround += 1
        print(check_list)
            




fn = 'Minisodoku01.txt'
# fn  = input('Enter Minisodoku0X.txt: ')
s = readMinisodoku(fn)
# checkMiniSodoku(s)
# print('running miniSodoku')
printMiniSodoku(s)
# res = checkMiniSodoku(s)