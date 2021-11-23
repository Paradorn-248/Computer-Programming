def read(filename) :
    with  open(filename) as f :
        data = [line.strip().split(',') for line in f]
        data2 = []
        data2.append(data[0])
        for i in range(1,len(data)) :
            add = []
            for j in range(len(data[0])-1) :
                add.append(int(data[i][j]))
            add.append(data[i][len(data[i])-1])
            data2.append(add)
    return data2
            
        # print(data2)
        # print(data)

def menu(m,data) :
    row = len(data)
    column = len(data[0])

    if m == 1 :
        print(len(data),end='')

    if m == 2 :
        max = 0
        res = ''
        for i in range(column-1) :
            sum = 0
            for j in range(1,row) :
                sum += data[j][i]
            if max <= sum :
                max = sum
                res = data[0][i]
        print(res,end='')

    if m == 3 : #blueplanet 5
        max_list = []
        for i in range(1,len(data)) :
            max_list.append(data[i][5])
        max_list.sort()
        max_list.reverse()
        print(max_list[0],max_list[1],max_list[2],end='')

    if m == 4 :
        user = ''
        max = 0
        for i in range(1,row) :
            sum = 0
            for j in range(column-1) :
                sum += data[i][j]
            if sum >= max :
                max = sum
                user = data[i][column-1]
        print(user,max,end = '')

    if m == 5 :
        user = ''
        max = 0
        for i in range(1,row) :
            if max <= data[i][0] :
                user = data[i][column-1]
                max = data[i][0]
        print(user,max,end = '')
 
    if m == 6 : # korea 17
        sum = 0
        for i in range(1,row) :
            if data[i][17] > 500 :
                sum += 1
        print(sum,end='')

    if m == 7 : #siam 7 food 4
        sum = 0
        for i in range(1,row) :
            if data[i][7] > data[i][4] :
                sum += 1  
        print(sum,end='')
    
    if m == 8 : #rajdumnern 26
        user = ''
        max = 0
        ratio = 0
        for i in range(1,row) :
            sum = 0
            for j in range(column-1) :
                sum += data[i][j]
            ratio = data[i][26]/sum
            if max <= ratio :
                user = data[i][column-1]
                max = ratio
        print(user,end='')

    if m == 9 :
        count = 0
        ratio = 0
        for i in range(1,row) :
            sum = 0
            a = []
            for j in range(column-1) :
                a.append(data[i][j])
                sum += data[i][j]
            a.sort()
            a.reverse()
            ratio = (a[0]+a[1])*100/sum
            if ratio > 70 :
                count += 1
        print(count,end='')

    if m == 10 : #pantip 36
        count = 0
        for i in range(1,row) :
            if data[i][36] == 0 :
                count += 1
        print(count,end='')
        

def search(data) :
    name = input('\nname: ')
    for i in range(len(data[0])) :
        if data[0][i] == name :
            print(i)


# filename = 'pantip_read_20181015_20181222.txt'
filename = input('File name: ')
m = int(input('enter number: '))
data = read(filename)
menu(m,data)
# search(data)