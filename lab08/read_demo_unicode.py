def demo_reader() :
    with open('unicode.txt','r') as f :
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_path() :
    with open(r'C:\computer programing\lab08\lab08_path\unicode2.txt','r') as f :
    #with open('C:\computer programing\\lab08\\lab08_path\\unicode2.txt','r') as f :
    #with open('C:/computer programing/lab08/lab08_path/unicode2.txt','r') as f :
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_unicode() :
    with open(r'C:\computer programing\lab08\lab08_path\province.txt',encoding = 'utf8') as f :
        data = f.read()
        print(data)

def demo_reader_unicode2() :
    with open(r'C:\computer programing\lab08\lab08_path\province.txt',encoding = 'utf8') as f :
        # i = 1
        # for line in f :
        #     print(f'{i}. {line}')
        #     i += 1
        for i,line in enumerate(f) :
            print(f'{i+1}. {line}',end='')

# demo_reader()
# demo_reader_path()
# demo_reader_unicode()
demo_reader_unicode2()