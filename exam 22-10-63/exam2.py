def fire1(n) :
    listt = []
    for i in range(n//2) :
        num = '1'
        space = ' '
        res = (2*(i))*space + num + (n-2-2*i)*space + num + (n-2-2*i)*space +num
        res = list(res)
        listt.append(res)
        # print(res)
    a = (num+space)*n
    # print(a)
    listt.append(list(a))
    listt2 = listt.copy()
    for i in range(len(listt)-1,-1,-1):
        # print(listt[i])
        listt2.append(listt[i])
    # print Star
    # for i in range(len(listt2)) :
    #     for j in range(len(listt2[i])) :
    #         print(listt2[i][j],end='')
    #     print()
    # print(listt2)
    return listt2

def fire2(n) :
    a = [[1]*(2*n-1) for i in range(2*n-1)]
    # print(a)
    i = 0
    j = 0
    tmp = 2*n-1
    for l in range(n,-1,-1) :
        for k in range(i,tmp-i) :
            for v in range(j,tmp-j) :
                a[k][v] = l
        i += 1
        j += 1
    # print(a)
    # print Heavy Rotation
    # for i in range(len(a)) :
    #     for j in range(len(a[0])) :
    #         print(a[i][j],end='')
    #     print()
    # print(a)
    return a

def printsky(res) :
    for i in range(len(res)) :
        for j in range(len(res[0])) :
            print(f'{res[i][j]}',end='')
        print()
        print()
    print()

sky = int(input('Sky : '))
hanabi = int(input('Hanabi : '))
sky = [['.']*sky**2 for i in range(sky)]
command = []
for i in range(hanabi) :
    r = input().strip().split() 
    for j in range(len(r)) :
        r[j] = int(r[j])
    command.append(r)
print(command)

# printsky(sky)
# fire1(5)
# fire2(5)