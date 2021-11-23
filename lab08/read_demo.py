def demo_reader() :
    f = open('flower.txt')
    data = f.read()
    print(data)
    f.close()

def demo_readline() :
    f = open('flower.txt')
    data = f.readline()
    print(data)
    data2 = f.readline()
    print(data2)
    data3 = f.readline()
    print(data3)
    f.close()

def demo_readlines() :
    f = open('flower.txt')
    data = f.readlines()
    print(data)
    f.close()

def demo_readline2() :
    f = open('flower.txt')
    for _ in range(3) :
        print(f.readline(),end='') #ถ้าไม่มีend=''จะเว้นบันทัดไป2รอบ เพราะprintมันเว้นบันทัด1รอบยุแล้ว
    f.close()

def demo_readlines2() :
    f = open('flower.txt')
    for line in f :
        print(line.capitalize(),end='') #ถ้าไม่มีend=''จะเว้นบันทัดไป2รอบ เพราะprintมันเว้นบันทัด1รอบยุแล้ว
    f.close()



# demo_reader()
# demo_readline()
# demo_readlines()
# demo_readline2()
# demo_readlines2()