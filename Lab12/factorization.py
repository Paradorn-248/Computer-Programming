n = int(input('n: '))
res = []

def prime(n) :
    if (n < 2):
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

i = 2
while True:
    if n == 1:
        break 
    if prime(i) :
        if n % i == 0 :
            res.append(i)
            n = n/i
            i = 2
            
        else :
            i += 1
    else :
        i += 1
    # print(n)
for i in res :
    print(i,end=' ')