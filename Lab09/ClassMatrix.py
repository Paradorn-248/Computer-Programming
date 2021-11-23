class Matrix :
    def __init__(self,data) :
        self.data = data

    def det(self) :
        sumlower = (self.data[0][0]*self.data[1][1]*self.data[2][2]) + (self.data[0][1]*self.data[1][2]*self.data[2][0]) + (self.data[0][2]*self.data[1][0]*self.data[2][1])
        sumupper = (self.data[2][0]*self.data[1][1]*self.data[0][2]) + (self.data[2][1]*self.data[1][2]*self.data[0][0]) + (self.data[2][2]*self.data[1][0]*self.data[0][1])
        return sumlower-sumupper
    
    def plus(self,B) :
        ans = [['']*3 for i in range(3)]
        for i in range(3) :
            for j in range(3) :
                ans[i][j] = self.data[i][j] + B.data[i][j]
        return Matrix(ans)

    def minus(self,B) :
        ans = [['']*3 for i in range(3)]
        for i in range(3) :
            for j in range(3) :
                ans[i][j] = self.data[i][j] - B.data[i][j]
        return Matrix(ans)

    def multiply(self,B) :
        ans = [[sum(self.data[i][k]*B.data[k][j] for k in range(len(self.data[0]))) for j in range(len(B.data[0]))] for i in range(len(self.data))]
        return Matrix(ans)

    def show(self) :    
        for i in range(3) :
            for j in range(3) :
                print(f'{self.data[i][j]:^6}', end = ' ')
            print()

# matA = [[1,2,3],[2,3,4],[4,5,6]]
# matB = [[6,7,8],[8,9,1],[1,2,3]]
def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()