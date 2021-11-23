import datetime

def demo_append() :
    with open('demoappend.txt','a',encoding = 'utf8' ) as f: #mode a คือ append
        f. write('lilly\n')

def cash_register() :
    with open('trans.txt','a',encoding = 'utf8') as f :
        d = {'m':'mocha','l':'latte','e':'espresso','c':'cappuccino'}
        while True :
            menu = input('[m]ocha, [l]atte, [e]spresso, [c]appuccino, [q]uit : ')
            if menu != 'q' :
                dt = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                f.write(f'{d[menu]},{dt}\n')
            else :
                break
            
# demo_append()
cash_register()