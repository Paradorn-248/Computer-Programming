n = int(input())

listt = [[1]*(2*n-1) for i in range(2*n-1)]

def print_mat(listt) :
    for i in range(len(listt)) :
        for j in range(len(listt)) :
            print(listt[i][j],end=' ')
        print()

for i in range(n-1) :
    for j in range(i,2*n-1-i) :
        listt[i][j] = n-i
        if j == i or j == 2*n-2-i :
            for k in range(i+1,len(listt)-i-1) :
                listt[k][j] = n-i

len_list = len(listt) #7
tmp = 0
k = n
for i in range(len_list-1,n-1,-1) :
    for j in range(tmp,len_list-tmp)  :
        listt[i][j] = k-tmp
    tmp += 1

print_mat(listt)
