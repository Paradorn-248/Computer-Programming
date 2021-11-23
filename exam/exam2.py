def check_not_prime(n) :
    for i in range(2,n) :
        if n % i == 0 :
            return True
        
num = 0
while num > 9999 or num < 99  :
    num = int(input('Enter an integer (99-9999): '))

count = 0
while count != 5 :
    if check_not_prime(num-2) != True and check_not_prime(num) != True :
        print(f'({num-2}, {num})')
        count += 1
    num -= 1
