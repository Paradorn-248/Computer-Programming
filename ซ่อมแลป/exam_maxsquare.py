def AreaInput(ss):
    now = ss.split()
    #row print(len(now))
    row = len(now)
    #col print(len(now[0]))
    col =len(now[0])
    ar = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            ar[i][j]=now[i][j]
    return ar

def maxArea(ss):
    row = len(ss)
    col = len(ss[0])
    high = min(row,col)
    ans= int(0)
    jue = False
    for a in range(high,0,-1):
        #print("*")
        for b in range(row-a):
            for c in range(col-a):
                #print("hi")
                if jue==True:
                    break
                #print("%d %d %d"%(a,b,c))
                plus = 0
                for d in range(b,b+a+1):
                    for e in range(c,c+a+1):
                        if ss[d][e]=='.':
                            plus+=1
                #print(plus)
                if(plus == (a+1)**2):
                    jue = True
                    for d in range(b, b + a + 1):
                        for e in range(c, c + a + 1):
                            ss[d][e] = 'o'
                    ans = (a+1)**2
                    #print("Jue")
    if jue ==True:
        return ans,ss
    else:
        for d in range(row):
            for e in range(col):
                if ss[d][e] == '.':
                    ss[d][e]='o'
                    ans = 1
                    return ans, ss
    return ans,ss

def printS(ss):
    for i in range(len(ss)):
        for j in range(len(ss[i])):
            print(ss[i][j], end='')
        print()

fn = input('Enter filename: ')
with open(fn) as f:
    s = f.read()
ss = AreaInput(s)
printS(ss)
res,ss = maxArea(ss)
print(f'max square area: {res}')
printS(ss)