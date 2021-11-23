       #
      ###
     #####
    #######
     #####
      ###
       # 
      #
     ###
    #####
     ###
      #

def upper_part(n) :
    round = n//2
    for i in range(round) :
        # for i in range(n+1) :
        space = ' ' * (round)
        # for i in range(n // 2) :
        star = '#' * (2*i + 1)
        n -= 1 
        round -= 1
        print(space+star)

def lower_part(n) :
    round = n // 2
    for i in range(n//2) :
        # for i in range(n) :
        space =  ' ' * (i+1)
        star = '#' * (2*(round-1) + 1)
        print(space+star)
        round -= 1

n = int (input('input: '))
upper_part(n)
print('#' * n)
lower_part(n)