def read(filename) :
    with open(filename) as f :
        data = [line.strip().split() for line in f]
        # print(data)
    return data

def plus(A,B):
     return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def minus(A,B):
     return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply(A,B):
     return [[sum(A[i][k]*B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
     
def print_matrix(res) :
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()
        
def cal_mat(data) :
    a,b = [],[]
    operator = list('+-*')
    i = 0
    j = 0
    while i <= len(data) :
        a.append(data[i])
        j = i
        if data[i][0] in operator :
            while data[j][0] :
                b.append(data[j+1])
    print(a,b)



filename = 'matrix.txt'
# filename = input('File name: ')
data = read(filename)
cal_mat(data)