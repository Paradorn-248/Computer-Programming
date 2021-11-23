def printS(ss) :
    for i in range(len(ss)) :
        for j in range(len(ss[i])) :
            print(ss[i][j],end='')
        print()

def parseInput(s) :
    res = [line.strip() for line in s]
    n = len(res)**(1/2)
    i = 0
    end = res.index('')
    space = res.count('') -1
    # print(end,space)
    # print(res)
    res2 = []
    for j in range(space) :
        add = []
        while res[i] != '':
            add.append(res[i])
            i += 1
        i +=1
        res2.append(add)
    add = []
    res2 = res2[:-1]
    for k in range(i+1,len(res)) :
        add.append(res[k])
    res2.append(add)
    # print(res2)
    return res2

def findMaxSquareArea(ss) :
    for i in range(len(ss)) :


# fn = input('Enter filename: ')
fn = 'Square01.txt'
with open(fn) as f :
    s = f.read()
ss = parseInput(s)
# print(ss)
printS(ss)
# res,ss = findMaxSquareArea(ss)
# print(f'max square area: {res}')
# print(ss)