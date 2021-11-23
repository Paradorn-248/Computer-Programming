def Add():
    n = int(input())
    A = [[0 for i in range(2*n-1)] for j in range(2*n-1)]
    return A,n

def change(A,n,i,j,x):
    for l in range(n,0,-1) :
        for a in range(i,len(A)-i):
            for b in range(j,len(A)-j):
                A[a][b] = l
        i += 1
        j += 1
    return A

def show(A):
    for i in A:
        for j in i:
            print(j, end = ' ')
        print()


A,n = Add()
show(change(A,n,0,0,n))