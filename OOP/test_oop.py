class Person :
    def __init__(self,name,age,money) :
        self.name = name 
        self.age = age 
        self.money = money

    def __str__(self) :
        return self.name + ' Watcharasemakul ' + str(self.age) + ' years old.'

    def __lt__(self,rhs) :
        if self.age != rhs.age :
            return self.age < rhs.age
        else :
            return self.name < rhs.name

    def print_person(self) :
        print(f'My name is {self.name}, {self.age} years old.')

    def same_money(self,other1,other2,other3) :
        return self.money & other1.money & other2.money & other3.money # & คือintersectของset

# using __init__
p1 = Person('Paradorn',18,{12,150,165,15})
p2 = Person('Ake',52,{20,15,21,140})
p3 = Person('Ladaporn',40,{263,214,32,15})
p4 = Person('Parada',18,{15,16,196,14})

# using __str__
p1.print_person()
print(p1)

print(p1.same_money(p2,p3,p4))
# using __lt__ (<)
if p2 < p1 :
    print(f'{p1.name} is older than {p2.name}')
else :
    print(f'{p2.name} is older than {p1.name}')

# using __lt__ (sort)
family = [p1,p2,p3,p4]
family.sort()
for i in range(len(family)) :
    print(family[i])