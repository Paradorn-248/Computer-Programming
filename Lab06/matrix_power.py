def zeroMat_mul_power(A,B):
  c = []
  for _ in range(len(A)):
    row = []
    for _ in range(len(B[0])):
      row.append(0)
    c.append(row)
  return c

def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()

def mul_matrix(A,B) :
  C = zeroMat_mul_power(A,A)
  for i in range(len(A)) :    
      for k in range(len(B[0])) :
        sum = 0 
        for j in range(len(A[0])) :
          sum += A[i][j] * B[j][k]
        C[i][k] = sum
  return C

def power_matrix(A,c) :
    tmp = A.copy()
    for _ in range(c-1) :
        tmp = mul_matrix(tmp,A)
    return tmp

# A = [[1,2,3],[4,5,6],[7,8,9]]
A = [[13,14],[15,16]]
c = 2

D = power_matrix(A,c)
print_matrix(D)