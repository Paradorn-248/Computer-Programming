def plusmat(a,b) :
    return [[float(a[i][j])+float(b[i][j])for j in range(len(a[0]))]for i in range(len(a))]

def minusmat(a,b) :
    return [[float(a[i][j])-float(b[i][j])for j in range(len(a[0]))]for i in range(len(a))]

def mulMat(a,b) :
    return [[sum(float(a[i][k])*float(b[k][j]) for k in range(len(a[0]))) for j in range(len(b[0]))]for i in range(len(a))]

def transpose(a) :
    return [[float(a[j][i]) for j in range(len(a))]for i in range(len(a[0]))]

def cons(c,a) :
    return [[c*float(a[i][j]) for j in range(len(a[0]))]for i in range(len(a))]

def powmat(a,c) :
    tmp = a
    for _ in range(1,c) :
        tmp = mulMat(tmp,a)
    return tmp

def read(filename) :
    with open(filename) as f :
        data = [line.strip().split() for line in f]
    return data

def printmat(res) :
    for i in range(len(res)) :
        for j in range(len(res[0])) :
            print(f'{res[i][j]:^10.2f}',end='   ')
        print()
    print()

def result1() :
    res1 = plusmat(transpose(A),cons(7,C))
    printmat(res1)
def result2() :
    res2 = mulMat(mulMat(B,B),B) #powmat(B,3)
    printmat(res2)
def result3() :
    res3 = minusmat(transpose(mulMat(A,B)),C)
    printmat(res3)
def result4() :
    res4 = mulMat(C,plusmat(transpose(C),cons(2,A)))
    printmat(res4)


filea = input()
fileb = input()
filec = input()
A = read(filea)
B = read(fileb)
C = read(filec)

result1()
result2()
result3()
result4()
# printmat(transpose(A))