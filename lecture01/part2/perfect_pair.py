def perfect_pair(data,pair) :
    sum = 0
    for i in range(len(data)-1) :
        for j in range(i+1,len(data)) :
            sum = data[i] + data[j]
            if sum <= 100 and sum >= -100 and sum not in pair:
                pair.append(sum)

def list_str_to_int(data) :
    for i in range(len(data)) :
        add = int(data[i])
        data_int.append(add) 

data = input('Input: ').strip().split()
data_int = []
pair = []
list_str_to_int(data)
perfect_pair(data_int,pair)
pair.sort()

for i in range(len(pair)) :
    print(pair[i],end = ' ')
