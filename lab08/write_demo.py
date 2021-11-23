#การwrite()จะเป็นการเขียนทับทั้งหมด

def write_demo() :
    f = open('demo.txt','w') #เราสามารถเลือกpathที่เราจะสร้างไฟล์เองได้ # ถ้าไม่ได้บอกว่าmodeอะไร จะdefaultให้เป็นmode r(read)
    f.write('hello Python\n') 
    f.write('I love Python.\n')
    f.write('Line3\n')
    f.close()

def write_path_demo() :
    # f = open('C:\computer programing\lab08\lab08_path\demo_path.txt','w') #เราสามารถเลือกpathที่เราจะสร้างไฟล์เองได้
    f = open(r'C:/computer programing/lab08/lab08_path/demo_path2.txt','w') #เราสามารถเลือกpathที่เราจะสร้างไฟล์เองได้ 
               # มีrหรือไม่มีก้ได้
    f.write('Good bye Python\n')
    f.write('I love Python.\n')
    f.write('Line3\n')
    f.close()

def write_demo_thai() :
    f = open('demo_thai.txt','w',encoding='utf8')# ถ้าจะเขียนภาษาไทยเราจะต้องเพิ่ม encoding='utf8'
    f.write('Hello ไพธอน\n')
    f.write('I love ไพธอน\n')
    f.write('Line3\n')
    f.close()
 
def write_context_manager() :
    with open('demo_thai2.txt','w',encoding='utf8') as f : # ถ้าเราใช้ with เราไม่ต้องclose() เพราะถ้าจบมันจะcloseให้เอง
        f.write('Hello ไพธอน\n')
        f.write('I love ไพธอน\n')
        f.write('Line3\n')

def write_list() :
    menu = ['mocha','latte','espresso']
    with open ('menu.txt','w',encoding='utf8') as f :
        for m in menu :
            # f.write(m + '\n')
            f.write('{}\n'.format(m.capitalize()))



# write_demo()
# write_path_demo()
# write_demo_thai()
# write_context_manager()
write_list()

