def harn(n,c) :
    res = 0
    if n % c >0 :
        res = n//c+1
    else :
        res = n//c
    return res

p1 = 500
p2 = 800
p5 = 1500
p15 = 3000
n = int(input('N: '))
tmp = n
price = 0
while n > 0 :
    if n >= 15:
        price += (n//15)*p15
        n = n % 15
    elif n == 4 :
        price += p5
        n = 0 
    elif n >= 5:
        price += (n//5)*p5
        n = n % 5
    elif n >= 2 :
        price += (n//2)*p2
        n = n % 2
    elif n >= 1 :
        price += n*p1
        n = 0

if price >= p15*harn(tmp,15) :
    price = p15*harn(tmp,15)
if price >= p5*harn(tmp,5) :
    price = p5*harn(tmp,5)
if price >= p2*harn(tmp,2) :
    price = p2*harn(tmp,2)
if price >= p1*harn(tmp,1) :
    price = p1*harn(tmp,1)

print(price)
    