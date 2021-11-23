def transpose_matrix(A) :
    C = zeroMat_transpose(A)
    for i in range(len(A[0])) : #2
        for j in range(len(A)) : #3
            C[i][j] = A[j][i]
    return C

# def zeroMat(A):
#     c = []
#     for _ in range(len(A[0])):
#         row = []
#         for _ in range(len(A)):
#             row.append(0)
#         c.append(row)
#     return c

def zeroMat_transpose(A):
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

A = [[1,2],[3,4],[5,6]]    

D = transpose_matrix(A)
print_matrix(D)


#------------------------------------------------------------------ อีกวิธีหนึ่ง
'''
def transpose_matrix(A) :
    res = []
    row = len(A)
    column = len(A[0])
    for i in range(column) :
        add = []
        for j in range(row) :
            add.append(A[j][i])
        res.append(add)
    return res
    
def print_matrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2],[3,4],[5,6]]    

D = transpose_matrix(A)
print_matrix(D)
'''