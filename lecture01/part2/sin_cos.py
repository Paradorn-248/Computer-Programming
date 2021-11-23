import math

def fac(n) :
    fac = 1
    i = 1
    while i <= n:
        fac *= i
        i += 1
    return fac
def sin(x) :
    sum_sin = 0
    n = 1
    while n <= 10 :
        sum_sin += (((-1)**(n-1)) * (x ** (2*n - 1))) / fac(2*n - 1)
        n += 1
    return sum_sin

def cos(x) :
    sum_cos = 0 
    n = 0
    while n <= 10 :
        sum_cos += (((-1)**n) * (x**(2*n))) / (fac(2*n))
        n += 1
    return sum_cos

degree = float(input('degree: '))
radian = degree * math.pi / 180
print(f'sin({degree:.2f}): {sin(radian):.10f}')
print(f'cos({degree:.2f}): {cos(radian):.10f}')
# print(fac(6))