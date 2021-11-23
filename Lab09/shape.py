class Rectangle :
    def __init__(self,l,w) :
        self.l = l
        self.w = w
    
    def area(self) :
        return self.l*self.w

    def perimeter(self) :
        return 2*self.l + 2*self.w

    def is_square(self) :
        if self.l == self.w :
            return 'This rectangle is square too.'
        else :
            return 'This rectangle is not square.'

class Triangle :
    def __init__(self,l1,l2,l3) :
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def area(self) :
        s = (self.l1+self.l2+self.l3)/2
        return (s*(s-self.l1)*(s-self.l2)*(s-self.l3))**(1/2)

    def perimeter(self) :
        return self.l1+self.l2+self.l3

    def is_right_triangle(self) :
        if self.l3 == (self.l1**2+self.l2**2)**(1/2) :
            return 'This triangle is right triangle too.'
        else :
            return 'This triangle is not right triangle.'

class Circle :
    def __init__ (self,r) :
        self.r = r

    def area(self) :
        pi = 3.14
        return pi*self.r**2

    def perimeter(self) :
        pi = 3.14
        return 2*pi*r

# Rectangle
l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)          
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

# Triangle
l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

# Circle
r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area():.2f}.')  
print(f'Perimeter is {p3.perimeter():.2f}.')  