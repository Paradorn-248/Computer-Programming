def plus(A,B):
     return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# print(plus([[1,2],[3,4]],[[5,6],[7,8]]))

def multiply(A,B):
     return [[sum(A[i][k]*B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

# print(multiply([[1,2],[3,4]],[[5,6],[7,8]]))

def transpose(A):
     return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print(transpose([[1,2],[3,4]]))