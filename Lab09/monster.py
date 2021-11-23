import numpy as np
X = np.random.RandomState(1)
class Player :
    def __init__(self,blood) :
        self.blood = blood
        self.attack = 10
        self.heal = 20

    def effect(self,act) :
        if act == 'a' :
            self.attack += 2
        elif act == 'h' :
            self.attack = 10

class Monster :
    def __init__(self,blood) :
        self.blood = blood

    def attack(self) :
        attack = X.randint(1, 100)
        return attack

blood = int(input('Blood Start: '))
player = Player(blood)
monster = Monster(blood)

while True:

    act = input('Attack(a) or Heal(h): ')
    #player act
    if act == 'a' :
        monster.blood -= player.attack
        if monster.blood > 0 :
            print(f"Monster's HP left {monster.blood}")    
        else :
            print(f"Monster's HP left 0")

    if monster.blood <= 0 :
        print('You win.(^_^)')
        break
    if act == 'h' :
        player.blood += 20
        print(f'Your HP left {player.blood}')
    player.effect(act)

    #monster act
    player.blood -= monster.attack()
    if player.blood <= 0 :
        print(f"Monster's turn : Your HP left 0")
    else :
        print(f"Monster's turn : Your HP left {player.blood}")

    if player.blood <= 0 :
        print('You lose and die.(T_T)')
        break
