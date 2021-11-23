n = 1
count = 0

while n != 0 :
    n = int(input())
    if n > 0 :
        count += 1

if count > 0 :
    print(f'I found {count} positive integer(s).')
else :
    print('No positive input!')