data = []
enter = 1
while True :
    enter = input().strip().split()
    if enter == [] :
        break
    else :
        for i in range(len(enter)) :
            enter[i] = int(enter[i])
        data.append(enter)

def cw(area) :
    row = len(area)
    column = len(area[0])
    min_cw = 999999999999
    for i in range(row-1) :
        for j in range(column-1) :
            price1 = area[i][j + 1] * 1.1
            price2 = area[i + 1][j] * 1.1 * 1.1 
            price3 = area[i + 1][j + 1] * 1.1
            sum_price = area[i][j] + price1 + price2 + price3
            # print(sum_price)
            if sum_price <= min_cw :
                min_cw = sum_price
    # print(f'{min_cw:.2f}')
    return min_cw

def ccw(area) :
    row = len(area)
    column = len(area[0])
    min_ccw = 99999999999999
    for i in range(1,row) :
        for j in range(column-1) :
            price1 = area[i][j + 1] * 1.1
            price2 = area[i - 1][j] * 1.1 * 1.1 
            price3 = area[i - 1][j + 1] * 1.1
            sum_price = area[i][j] + price1 + price2 + price3
            # print(sum_price)
            if sum_price <= min_ccw :
                min_ccw = sum_price
    # print(f'{min_ccw:.2f}')
    return min_ccw

# cw(data)
# ccw(data)
# print(data)
for i in range(len(data)) :
    len_data = len(data[0])
    if len_data != len(data[i]):
        print("Can't Buy")
        exit()

if ccw(data) <= cw(data) :
    print(f'{ccw(data):.2f}')
else :
    print(f'{cw(data):.2f}')