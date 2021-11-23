def anytoten(any,n) :
    '''ทางลัด
    ten = int(any,n)'''
    ten = 0
    len_any = len(any)
    char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(len_any) :
        if any[i] in char :
            add = 10 + ord(any[i])-65
        else :
            add = int(any[i])
        ten += add*(n**(len_any-i-1))
    return ten

def tentoany(ten,m) :
    num = ten
    listt = []
    char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while num > 0 :
        remain = num % m
        if remain >= 10 :
            listt.append(char[remain-10])
        else :
            listt.append(remain)
        num = num // m
    listt.reverse()
    res = ''
    for i in range(len(listt)) :
        res += str(listt[i])
    return res

n = int(input())
m = int(input())
any = input()
anytoten(any,n)
ten = anytoten(any,n)
# print(ten)
print(tentoany(ten,m))