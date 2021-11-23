class Medal :
    def __init__(self,country,gold,silver,bronze) :
        self.country = country
        self.gold = gold 
        self.silver = silver
        self.bronze = bronze

    def total(self) : #instance method
        return self.gold + self.silver + self.bronze

    def test(self) :
        print("sasdwawd")

class Athlete :
    def dummy(self) :
        return 'Hello'

thai = Medal('Thailand',5,1,3)
print(thai.total())
thai.test()