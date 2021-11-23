class Person :
    def __init__ (self) :
        self.fname = ''
        self.lname = ''
        self.country = 'Thailand'

    # มี __init__ 2อันไม่ได้ แต่java มีได้
    # def __init__(self,fname,lname,country) :
    #     self.fname = fname
    #     self.lname = lname
    #     self.country = country

class Person2 :
    def __init__(self,fname=None,lname=None,country='Thailand') :
        self.fname = fname
        self.lname = lname
        self.country = country

    def __str__(self) :
        return f'fname: {self.fname}, lname: {self.lname}, country: {self.country}'

# p1 = Person()
# print(p1.fname)
# print(p1.country)

# p1 = Person2()
# print(p1.fname) 
# print(p1.country) 

# p2 = Person2(fname='Peter')
# print(p2.fname)

p3 = Person2('Peter','Parker')
print(p3)

p4 = Person2(fname='Swift',lname='Taylor',country='USA')
print(p4)