def zeroMat(A):
  c = []
  for i in range(len(A)):
    row = []
    for _ in range(len(A[i])):
      row.append(0)
    c.append(row)
  return c
  
def minus_matrix(A,B) :
  C = zeroMat(A)
  for i in range(len(A)) :
    for j in range(len(A[0])) :
      C[i][j] = A[i][j] - B[i][j]
  return C

def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]

D=minus_matrix(A,B)
print_matrix(D)