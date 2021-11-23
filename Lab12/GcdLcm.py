a = int(input('a : '))
b = int(input('b : '))

# def gcd(a,b) : # a=min b=max
#     for i in range(1,a+1) :
#         if a%i==0 and b%i==0 :
#             res = i
#     return res

def gcd(a,b) :
    if b == 0 :
        return a
    return gcd(b,a%b)

lcm = a*b/gcd(a,b)
print(f'GCD : {gcd(a,b)}')
print(f'LCM : {int(lcm)}')