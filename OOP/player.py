class Player :
    def __init__(self) : #dunder -> double underscores
        self.fname = '' 
        self.lname = ''
        self.number = ''

class Player2 :
    def __init__(self,fname,lname,number) :
        self.fname  = fname
        self.lname = lname 
        self.number = number 

p1 = Player()
p1.fname = 'Loris '
p1.lname = 'Karius'
p1.number = 1

p2 = Player()
p2.fname = 'Alex'
p2.lname = 'Manninger'
p2.number = 13 

p1a = Player2('Loris','Karius',1)
p2a = Player2('Alex','Manninger',13)

print(p1a.fname)
print(p2a.lname)
