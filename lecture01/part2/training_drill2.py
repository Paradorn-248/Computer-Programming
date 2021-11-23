day = int(input('Day: '))
sum = 0
last = 1
listt =[]

for i in range(day) :
    sum = sum + last
    listt.append(sum)
    last = sum - last

for i in range(len(listt)) :
    print(listt[i],end=(' '))