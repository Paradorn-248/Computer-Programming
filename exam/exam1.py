string = input('Enter a string: ')
pos = -1
while pos <= 0 :
    pos = int(input('Enter a positive integer: '))

print('012345678901234567890123456789')
def upper(string,pos) :
    space = ' '
    for i in range(pos-1) :
        print(space * (i+1) + string)

def lower(string,pos) :
    space = ' '
    pos_use = pos - 1
    for i in range(pos - 1):
        print(space * pos_use + string)
        pos_use -= 1


upper(string,pos)
print(' '*pos+string)
lower(string,pos)