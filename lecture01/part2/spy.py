data = input().strip().split()
intdata = []
string = ''

for i in range(len(data)) :
    add = int(data[i])
    intdata.append(add)
# print(intdata[0])
for i in range(1,len(data),intdata[0]+1) :
    a = f'{intdata[i]:c}'
    # print(a)
    string += a

print(string)