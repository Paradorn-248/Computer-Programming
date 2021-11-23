def find(n) :
    for i in range(len_a) :
        if a[i] == n :
            return True
    else :
        return False



a = [4,8,57,16,23,42,15]
n = int(input('Enter an integer: '))
# n = 43
len_a = len(a)
if find(n) == True :
    print(f'Found {n}')

else :
    print(f'Not found {n}')
