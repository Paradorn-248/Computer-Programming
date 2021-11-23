n = int(input('Day: '))
last = 1
sum = 0
lis = []
for i in range(n) :
    sum += last
    lis.append(sum)
    last = sum - last

for i in range(n) :
    print(lis[i],end =' ')
