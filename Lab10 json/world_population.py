import json 
def read_data(filename) :
    with open(filename) as f :
        data = f.read()
        # print(data) 
        # print(type(data))
        data = json.loads(data)
        # print(data)   
        # print(type(data))
    return data

def menu(m,data) :
    len_data = len(data)
    if m == '1' :
        print(len_data,end='')
    
    if m == '2' :
        sum = 0
        for i in range(len_data) :
            sum += int(data[i]['population'])
        print(sum,end='')
    
    if m == '3' :
        sum_c = 0
        sum_five = 0
        for i in range(len_data) :
            if data[i]['country'][0] == 'C' :
                sum_c += 1
            if len(data[i]['country']) > 5 :
                sum_five += 1
        print(sum_c)
        print(sum_five,end='')

    if m == '4' :
        more_500,betw,min_10 = 0,0,0
        for i in range(len_data) :
            if int(data[i]['population']) > 500000000 :
                more_500 += 1
            if int(data[i]['population']) > 250000000 and int(data[i]['population']) < 750000000 :
                betw += 1
            if int(data[i]['population']) < 10000000 :
                min_10 += 1
        print(more_500)
        print(betw)
        print(min_10,end='')

    if m == '5' :
        sum_20 = 0
        sum_50_150 = 0
        for i in range(20) :
            sum_20 += float(data[i]['World'])
        # per = sum_20 * 100 / sum_pop
        for i in range(49,150) :
            sum_50_150 += float(data[i]['World'])
        # per2 = sum_50_150 * 100 / sum_pop
        # print(sum_pop)
        print(f'{sum_20*100:.2f}')
        print(f'{sum_50_150*100:.2f}',end='')

# filename = input('File Name: ')
filename = 'worldpopulation.json'
data = read_data(filename)
# print(data)
m = input('Input : ')
menu(m,data)