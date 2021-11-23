data = []
min = 9999999999
max = -9999999999
count_pos = 0
while count_pos != 5 :
    n = int(input('Enter a positive number: '))
    if n > 0 :
        if min > n :
            min = n
        if max < n :
            max = n
        count_pos += 1
        data.append(n)
data.sort()
print(f"sum: {sum(data)}")
print(f"min: {min}")
print(f"max: {max}")
print(f"med: {data[2]}")