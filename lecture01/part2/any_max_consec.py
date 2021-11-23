count = 0
n = 1
sum = 0
a = []
j = 1

while n != 0:
    n = int(input())
    a.append(n)

if a[0] == 0 :
    print('0')
    print('0')
    exit()

count_list = []
max_list = []

for i in range(len(a)-1) :
    if a[i] == a[j] :
        count += 1
        j += 1
    else :
        if count != 0 :
            count_list.append(count + 1)
            max_list.append(count+1)
        elif count == 0 :
            max_list.append(1)
        count = 0
        j = j + 1

b = sorted(count_list)
i = 0

if len(b) > 0:
    while max_list[i] != b[len(b)-1] :
        sum += max_list[i]
        i += 1

else :
    print('1')
    print(a[0])
    exit()


print(b)
print(count_list)
print(max_list)

print(b[len(b)-1])
print(a[sum])