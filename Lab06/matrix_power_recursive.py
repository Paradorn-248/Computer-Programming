def zeroMat(A):
  c = []
  for _ in range(len(A[0])):
    row = []
    for _ in range(len(A)):
      row.append(0)
    c.append(row)
  return c


def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()

def mul_matrix(A,B) :
    C = zeroMat(A)
    for i in range(len(A)) :    
        for k in range(len(A[0])) :
            sum = 0 
            for j in range(len(A[0])) :
                sum += A[i][j] * B[j][k]
            C[i][k] = sum
    return C
    

def power_matrix(a,c) :
    C = a
    if c == 1 :
        return C
    d = mul_matrix(C,A)
    return power_matrix(d,c-1)


A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2


D = power_matrix(A,c)
print_matrix(D)