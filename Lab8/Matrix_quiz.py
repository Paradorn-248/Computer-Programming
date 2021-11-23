def read(filename) :
    with open(filename) as f :
        data = f.readlines()
        res = [line.strip().split() for line in data]
        for i in range(len(res)) :
            for j in range(len(res[i])) :
                if res[i][j] != '+' and res[i][j] != '*' :
                    res[i][j] = int(res[i][j]) 
        print(res)
        operator = [['-'],['+'],['*'],['/']]
        index = 0
        a = []
        while res[index] not in operator:
            if res[index] != [] :
                a.append(res[index])
                index += 1
            else :
                index += 1
        print(a)
        index += 1

        b = []
        while res[index] not in operator:
            if res[index] != [] :
                b.append(res[index])
                index += 1
            else :
                index += 1
        print(b)
        index += 1
        c = []
        while res[index] not in operator:
            if index >= len(res) :
                break
            if res[index] != [] :
                c.append(res[index])
                index += 1
            else :
                index += 1
        print(c)
        return a,b,c

def multiply(A,B):
     return [[sum(A[i][k]*B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def plus(A,B):
     return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def print_matrix(mat) :
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()



# filename = input('File name: ')
filename = 'testcase.txt'
a,b,c = read(filename)
res = plus(c,multiply(a,b))
print_matrix(res)