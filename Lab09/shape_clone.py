class Rectangle :
    def __init__(self,l,w) :
        self.l = l
        self.w = w

    def area(self) :
        return self.l*self.w

    def perimeter(self) :
        return 2*(l+w)

    def is_square(self) :
        if l == w :
            return 'This rectangle is square too.'
    
class Triangle :
    def __init__(self,)


l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 