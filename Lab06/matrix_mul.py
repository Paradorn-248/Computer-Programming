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

# A = [[1,2,3],[4,5,6]]
# B = [[22,13],[54,43],[23,78]]
A = [[1,2,3],[4,5,6],[7,8,9]]  
B = [[22,13,23],[54,43,21],[23,78,71]]
D = mul_matrix(A,B)
print_matrix(D)