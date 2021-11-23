def plus_score(arr) :
    sum = 0
    max = 0
    min = 999999999999999
    for i in range(1,len(arr)) :
        arr[i] = int(arr[i])
        if max < arr[i] :
            max = arr[i]
        if min > arr[i]  :
            min = arr[i]
        sum += arr[i]
    res = sum - max - min 
    print(res)
    return res

def reader(filename) :
    with open(filename) as f :
        # data = f.readlines()
        # data2 = [line.split() for line in data]
        data2 = [line.split() for line in f]
        print(data2)
    return data2

filename = input('File name: ')
data = reader(filename)
name = []
score = []
len_data = len(data)
for i in range(len_data) :
    name.append(data[i][0])
    score.append(plus_score(data[i]))

max_score = max(score)
print(max_score)
for i in range(len_data) :
    if max_score == score[i] :
        print(name[i])