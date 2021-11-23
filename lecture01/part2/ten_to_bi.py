n = int(input('Enter number :'))
bi = []
checker = n
while n > 0 :
    bi.append(n % 2)
    n = n // 2

bi.reverse()
for i in range(len(bi)) :
    print(bi[i],end='')
print()
print(f'check : {checker:b}')
print(int('101101101',2))