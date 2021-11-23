# filename = input('File name: ')
filename = 'testcase.txt'
with open(filename) as f:
    a = [i.strip().split() for i in f.readlines() if i.strip().split()!=[]]

print(a)

def readMat(a):
    mat,op,line=[],[],[]
    for i in a:
        if i in [['+'],['*'],['-']]:
            mat.append(line)
            line=[]
            op.append(i)
        else :line.append(i)
    if len(line)>0: mat.append(line)
    # print(mat,op)
    print(op)
    return mat,op

# def zeroMat(r,c):
#     return [[0 for j in range(c)] for i in range(r)]

def plusMat(A,B):
    return [[int(A[i][j])+int(B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
#     res=zeroMat(len(a),len(a[0]))
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             res[i][j] = int(a[i][j]) + int(b[i][j])
#     return res

def minusMat(A,B):
    return [[int(A[i][j])-int(B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]

#     res=zeroMat(len(a),len(a[0]))
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             res[i][j] = int(a[i][j]) - int(b[i][j])
#     return res

def mulMat(A,B):
    return [[sum(int(A[i][k])*int(B[k][j]) for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
#     res=zeroMat(len(a),len(b[0]))
#     for i in range(len(a)):
#         for j in range(len(b[0])):W
#             sum=0
#             for k in range(len(a[0])):
#                 sum+= int(a[i][k])*int(b[k][j])
#             res[i][j]=sum
#     return res


def cal(mat,op):
    for i in range(len(op)):
        if '+' in op[i]:
            mat[i+1] = plusMat(mat[i],mat[i+1])
        elif '-' in op[i]:
            mat[i+1] = minusMat(mat[i],mat[i+1])
        elif '*' in op[i]:
            mat[i+1] = mulMat(mat[i],mat[i+1])
        res=mat[i+1]
    return res

def printMat(res) :
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()

mat,op = readMat(a)
res = cal(mat,op)
printMat(res)