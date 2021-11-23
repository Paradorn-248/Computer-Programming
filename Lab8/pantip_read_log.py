def read(filename) :
    with open(filename) as f :
        data = f.readlines()
        data2 = [line.strip().split() for line in data]
        data3 = []
        for i in range(len(data2)) :
            data3.append(data2[i][0].split(','))
        # print(data3)
    return data3

def menu_fn(choice,data) :
    if choice == '1' :
        print(len(data),end= '')

    if choice == '2' :
        sum = 0
        max = 0
        show_max = ''
        for i in range(len(data[1])-1) : #column
            sum = 0
            for j in range(1,len(data)) : #row
                sum += int(data[j][i])
            if max <= sum :
                max = sum
                show_max = data[0][i]
            # print(sum)
        print(show_max,end = '')

    if choice == '3' :
        a = []
        for i in range(1,len(data)) :
            a.append(int(data[i][5]))
        b = sorted(a)
        b.reverse()
        # print(b)
        print(b[0],b[1],b[2],end='')

    if choice == '4' :
        sum = 0
        max = 0
        show_max = ''
        for i in range(1,len(data)) : #row
            sum = 0
            for j in range(len(data[1])-1) : #column
                sum += int(data[i][j])
            if max <= sum :
                max = sum
                show_max = data[i][len(data[1])-1]
            # print(sum)
        print(show_max,max,end = '')

    if choice == '5' :
        max = 0
        name = ''
        for i in range(1,len(data)) :
            if max < int(data[i][0]) :
                max = int(data[i][0])
                name = data[i][len(data[1])-1]
        print(name,max,end ='')

    if choice == '6' :
        count = 0
        for i in range(1,len(data)) :
            if int(data[i][17]) > 500 :
                count += 1
        print(count,end ='')

    if choice == '7' : #food 4    siam 7
        count = 0
        for i in range(1,len(data)) :
            if int(data[i][7]) > int(data[i][4]) :
                count += 1
        print(count,end='')

    if choice == '8' : #rajdumnern 26
        max_ratio,sum_data = 0,0
        name = ''
        for i in range(1,len(data)) : #row
            for j in range(len(data[1])-1) : #column
                sum_data += int(data[i][j])
            ratio = int(data[i][26]) / sum_data
            if max_ratio < ratio :
                name = data[i][len(data[1])-1]
                max_ratio = ratio
            sum_data = 0
        print(name,end ='')

    if choice == '9' :
        sum_data,count = 0,0
        for i in range(1,len(data)) : #row
            a= []
            for j in range(len(data[1])-1) : #column
                a.append(int(data[i][j]))
                sum_data += int(data[i][j])                
            a.sort()
            a.reverse()
            # print(a)
            # print(sum_data)
            ratio = (a[0]+a[1]) * 100  / sum_data
            # print(ratio)
            if ratio > 70 :
                count += 1
            sum_data = 0
        print(count,end='')
                
    if choice == '10' : #pantip 36
        count = 0
        for i in range(1,len(data)) :
            if int(data[i][36]) <= 0 :
                count += 1
        print(count,end= '')

def search(data) :
    want = 1
    while want != 'q' :
        want = input('\n'+'Search: ')
        for i in range(len(data[0])) :
            if data[0][i] == want :
                print(i)


filename = 'pantip_read_20181015_20181222.txt'
# filename = input('File name: ')
menu = input('enter number: ')
data = read(filename)
# print(data)
menu_fn(menu,data)
# search(data)