# plus
def plus_matrix(A,B) :
    C = zeroMat(A)
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            C[i][j] = A[i][j] + B[i][j]
    return C

def zeroMat(A):
    c = []
    for i in range(len(A)):
      row = []
      for _ in range(len(A[i])):
        row.append(0)
      c.append(row)
    return c

# minus
def minus_matrix(A,B) :
    C = zeroMat(A)
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            C[i][j] = A[i][j] - B[i][j]
    return C

#transpose
def transpose_matrix(A) :
    C = zeroMat_transpose(A)
    for i in range(len(A[0])) : #2
        for j in range(len(A)) : #3
            C[i][j] = A[j][i]
    return C

def zeroMat_transpose(A):
    c = []
    for _ in range(len(A[0])):
        row = []
        for _ in range(len(A)):
            row.append(0)
        c.append(row)
    return c

# mul and power
def mul_matrix(A,B) :
  C = zeroMat_mul_power(A,B)
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

def zeroMat_mul_power(A,B):
  c = []
  for _ in range(len(A)):
    row = []
    for _ in range(len(B[0])):
      row.append(0)
    c.append(row)
  return c

# print matrix
def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()



A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2
# print_matrix(zeroMat_mul_power(C,C))
res = mul_matrix(plus_matrix(A,transpose_matrix(B)), minus_matrix(power_matrix(C,2),D))
# res = plus_matrix(A,transpose_matrix(B))
print_matrix(res)