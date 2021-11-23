class MyMath :
    def __init__(self) :
        self.pi = 3
        j = 2
        for i in range(1,51) :
            self.pi += ((-1)**(i+1))*4/((j)*(j+1)*(j+2))
            j += 2

    def is_even(self,num) :
        if num % 2 == 0 :
            return True
        return False

    def fac(self,num) :
        fac = 1
        for i in range(2,num+1) :
            fac = fac * i
        return fac

    def is_prime(self,num) :
        for i in range(2,num) :
            if num % i == 0 :
                return False
        return True

    def divide_by(self,num,k) :
        if num % k == 0 :
            return True
        return False

    def ten_to_bi(self,num) :
        res = ''
        base = 2
        while num > 0 :
            res += str(num%base) 
            num = num//base
        res = res[-1:-len(res)-1:-1]
        return res

    def ten_to_oct(self,num) :
        res = ''
        base = 8
        while num > 0 :
            res += str(num%base) 
            num = num//base
        res = res[-1:-len(res)-1:-1]
        return res
    
    def ten_to_sixteen(self,num) :
        res = ''
        base = 16
        char = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while num > 0 :
            if num%base < 10 :
                res += str(num%base)
            else :
                res += char[num%base]
            num = num//base
        res = res[-1:-len(res)-1:-1]
        return res
    
    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if my_math.divide_by(num,k):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')