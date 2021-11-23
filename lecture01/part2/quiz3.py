def pi(n) :
    sum = 3
    i = 2
    count = 2
    while count <= n :
        if count%2 == 0 :
            sum += 4 / (i*(i+1)*(i+2))
        else :
            sum -= 4 / (i*(i+1)*(i+2))
        i += 2
        count  += 1
    return sum 
    
n = int(input('n: '))
print(f'PI: {pi(n):.10f}')
