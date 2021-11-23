def readlines() :
    with open("grade.txt") as f :
        lines = [line.strip().split(',') for line in f]
        print(lines)

def read() :
    with open('grade.txt') as f :
        r = f.read()
        print(r)

def helper() :
    with open('grade.txt','a') as f :
        helper = '1'
        while helper != '0' :
            helper = input('Score: ')
            f.write('\n' + helper)


menu = input('Has helper? :')
menu.lower()
if menu == 'y' :
    helper()
    read()

elif menu == 'n' :
    read()