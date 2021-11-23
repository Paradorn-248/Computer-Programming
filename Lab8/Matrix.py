def read(filename) :
    with open(filename) as f :
        data = f.readlines()
        res = [line.strip().split() for line in data]
        for i in range(len(res)) :
            for j in range(len(res[i])) :
                if res[i][j] != '+' and res[i][j] != '*' :
                    res[i][j] = int(res[i][j]) 
        # print(res)
        a = []
        for i in range(3) :
            a.append(res[i])
        # print(a)
        b = []
        for i in range(4,9) :
            b.append(res[i])
        # print(b)
        c = []
        for i in range(10,13) :
            c.append(res[i])

        # print(c)
    return a,b,c

def multiply(A,B):
     return [[sum(A[i][k]*B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def plus(A,B):
     return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def print_matrix(mat) :
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()



filename = input('File name: ')
a,b,c = read(filename)
res = plus(c,multiply(a,b))
print_matrix(res)