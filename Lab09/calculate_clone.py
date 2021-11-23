class MyMath :
    def __init__(self) :
        self.pi = 3
        j = 2
        for i in range(1,51) :
            self.pi += ((-1)**(i+1))*4/((j)*(j+1)*(j+2))
            j += 2
        
    def is_even(self,num) :
        if num % 2 == 0 :
            return 'This number is even number.'
        else :
            return 'This number is not even number.'
    
    def factorial(self,num) :
        res = 1
        if num > 20 :
            return 'factorial TOO LONG.'
        for i in range(1,num+1) :
            res *= i
        return f'factorial is {res}.'

    def is_prime(self,num) :
        for i in range(2,num) :
            if num % i == 0:
                return 'This number is not a prime number.'
        return 'This number is a prime number.'

    def divide_by(self,num,k) :
        if num % k == 0 :
            return f'{num} is divisible by {k}.'
        return f'{num} is not divisible by {k}.'

    def ten_to_bi(self,num) :
        res = ''
        show = num
        while num > 0 :
            res += str(num%2)
            num = num//2
        res = res[-1:-len(res)-1:-1]
        return f'{show} is {res} in base 2.'
        
    def ten_to_oct(self,num) :
        res = ''
        show = num
        while num > 0 :
            res += str(num%8)
            num = num//8
        res = res[-1:-len(res)-1:-1]
        return f'{show} is {res} in base 8.'
        
    def ten_to_sixteen(self,num) :
        res = ''
        show = num
        char = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while num > 0 :
            if num % 16 >= 10 :
                res += char[num%16]
            else :
                res += str(num%16)
            num = num//16
        res = res[-1:-len(res)-1:-1]
        return f'{show} is {res} in base 16.'
        


my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

print(my_math.factorial(num))
print(my_math.ten_to_sixteen(num))
print(f'PI is {my_math.pi}')