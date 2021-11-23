# string = input('Input sentence: ')
string = 'WeAreTheChampion'
row = int(input('Input row: '))

def find_column(row) :
    sum = 0
    column = 1
    while True :
        sum += row
        if sum >= len(string) :
            return column
        else :
            column += 1
        for _ in range(row - 2) :
            sum += 1
            if sum < len(string) :
                column += 1
            elif sum >= len(string) :
                return column

zero_column = find_column(row)
print(find_column(row))

zero_arr = [['']*zero_column for i in range(row)]
i,j = 0,0
str_index = 0
count = 0
nub = 0
#ทำแท่งก่อน
while str_index <= len(string):
    zero_arr[j][i] = string[str_index]
    # print(zero_arr[j][i])
    str_index += 1
    nub += 1

    i += row-1
    count += 1

print('count',count)

j = 1
str_index = row
# ทำเฉียง
for _ in range(count-1) :
    i = row - 2
    for _ in range(row-2) :
        zero_arr[i][j] = string[str_index]
        i -= 1
        j += 1
        str_index += 1
    j += 1
    str_index += 1
# int(((zero_column-(count*row))/(row-2)))

print(zero_arr)
# for i in range(row) :
#     for j in range(zero_column) :
#         print(zero_arr[i][j],end='')
#     print()