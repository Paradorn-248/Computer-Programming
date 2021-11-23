class Medal :
    def __init__ (self,country,gold,silver,bronze) :
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self) : #instance method
        return self.gold + self.silver + self.bronze

    def __str__(self) : #toString()
        return f'{self.country:10}g: {self.gold:<3}, s: {self.silver:<3}, b: {self.bronze:<3}'

    def __repr__(self) : #string representation #ถ้าเป็นstringจะมี'',"" แต่ถ้าเป็นstrจะไม่มี
        return f'{self.__class__.__name__}{repr((self.country,self.gold,self.silver,self.bronze))}'
    #{self.__class__.__name__} -> บอกชื่อclass
    # ถ้ามีทั้งstr,reprจะเรียกใช้strก่อน

th = Medal('Thailand',5,6,10)
# print(th)

m = [
    Medal('Thailand',5,6,10),
    Medal('Japan',15,20,10),
    Medal('China',55,40,105)
    ]

for c in m :
    print(c)