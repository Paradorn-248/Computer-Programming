def read(filename) :
    with open(filename) as f :
        data = [line.split() for line in f]
        # print(data)
    return data

def sum_score(data) :
    sum = 0
    max = 0
    min = 99999999
    for i in range(1,len(data)) :
        data[i] = int(data[i])
        if max <= data[i] :
            max = data[i]
        if min >= data[i] :
            min = data[i] 
        sum += data[i]
    sum = sum - max - min
    return sum

    
# filename = 'Example.txt'
filename = input('File name: ')
data = read(filename)
score = []
name = []
for i in range(len(data)) :
    tmp_score = sum_score(data[i])
    score.append(tmp_score)
    name.append(data[i][0])
max_score = max(score)
print(max_score)
for i in range(len(data)) :
    if max_score == score[i] :
        print(name[i])

