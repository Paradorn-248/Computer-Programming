n = 1
count_pos = 0
count_neg = 0
sum_pos = 0
sum_neg = 0

while n != 0 :
    n = int(input('Enter an integer [or 0 to end]: '))

    if n > 0 :
        count_pos += 1
        sum_pos += n

    elif n < 0:
        count_neg += 1
        sum_neg += n

if count_pos == 0 and count_neg == 0 :
    print('Nothing else..')

if count_pos > 0 :
    print(f'average+: {sum_pos/count_pos:.2f}')

if count_neg > 0:
    print(f'average-: {sum_neg/count_neg:.2f}')