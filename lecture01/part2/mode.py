num = input('Enter list of numbers: ').strip().split()
maxnum = 0
countmax = 1
maxlist = []
countlist = []
numlist = []
# print(num)
for i in range(len(num)) :
    if num[i] not in maxlist :
        maxlist.append(num[i])
        
for i in range(len(maxlist)) :
    numlist.append(num.count(maxlist[i]))
    print(numlist)
max = 0

for i in range(len(numlist)) :
    if max <= numlist[i] :
        max = numlist[i]
count = 0
for i in range(len(numlist)) :
    if max != numlist[i] :
        count += numlist[i]

print(maxlist)

print(num[count])