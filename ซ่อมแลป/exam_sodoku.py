def printMiniSodoku(a):
    res, n = '',len(a)
    for i in range(n):
        for j in range(n):
            res += f'{a[i][j]:>3}'
        if i < n-1:
            res += '\n'
    print(res)
    
def readMiniSodoku(fn):
    f = open(fn)
    r = f.readlines()
    lis = [i.strip().split(',') for i in r if i.split() != '']
    return lis 
    
def checkMiniSodoku(lis):
    size = int(len(lis[0]))
    subsize = int(size ** 0.5)
    check1 = True
    ### case 1
    for a1 in range(0,size,subsize):
        for a2 in range(0,size,subsize):
            s = list()
            for i in range(0,subsize):
                for j in range(0,subsize):
                    if lis[a1+i][a2+j] in s : 
                        check1 = False 
                    else : s.append(lis[a1+i][a2+j]) 
            if check1 == False :
                print("Subgrid")
                subgrid = [[0]*subsize for i in range(subsize)]
                for e in range(0,subsize):
                    for g in range(0,subsize):
                        subgrid[e][g] = lis[a1+e][a2+g]
                printMiniSodoku(subgrid)
                print("fails test#1!")
                return False
                
    pattern = list()
    
    for a1 in range(0,size,subsize):
        for a2 in range(0,size,subsize):
            s = []
            for i in range(0,subsize):
                for j in range(0,subsize):
                    s.append(lis[a1+i][a2+j])
            if s in pattern : 
                print("Subgrid")
                c=0
                subgrid = [[0]*subsize for i in range(subsize)]
                for i in range(0,subsize):
                    for j in range(0,subsize):
                        subgrid[i][j] = s[c]
                        c+=1
                printMiniSodoku(subgrid)
                return False
            else : pattern.append(s)
        
    return True



############################################################
# fn = 'Minisodoku06.txt'
fn = input()
s = readMiniSodoku(fn)
print("running minisodoku")
printMiniSodoku(s)
res = checkMiniSodoku(s)
print(res)