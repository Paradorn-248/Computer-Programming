def mul_const(A,c) :
    C = zeroMat(A)
    for i in range(len(A)) :
        for j in range(len(A[i])) :
           C[i][j] = A[i][j] * c
    return C

def zeroMat(A):
    c = []
    for i in range(len(A)):
        row = []
        for _ in range(len(A[i])):
          row.append(0)
        c.append(row)
    return c
  

def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2],[3,4],[5,6]]
c = 2

D=mul_const(A,c)
print_matrix(D)