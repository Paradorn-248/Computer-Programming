N = int(input('N: '))

def check_prime(N) :
    count = 0
    dev = 3
    if N % 2 == 0:
        return False
    while dev < N :
        if N % dev == 0 :
            count += 1
        dev += 1

    if count > 0 :
        return False
    else :
        return True
        
while True:
    if check_prime(N) == True and check_prime(N+2) == True :
        print(f'({N}, {N+2})')
        break
    else :
        N += 1

