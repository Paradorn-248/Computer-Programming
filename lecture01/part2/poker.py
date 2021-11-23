num = input('Cards: ').strip().split()
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
    
# print(numlist)
max = 0

for i in range(len(numlist)) :
    if max <= numlist[i] :
        max = numlist[i]
count = 0
for i in range(len(numlist)) :
    if max != numlist[i] :
        count += numlist[i]

# print(maxlist)
countsam = countsong = countsee = 0

for i in range(len(numlist)) :
    if numlist[i] == 3 :
        countsam += 1

    if numlist[i] == 2 :
        countsong += 1

    if numlist[i] == 4 :
        countsee += 1

if countsee == 1 :
    print('Mark got "Four of a kind"')
elif countsam == 1 :
    if countsong == 0 :
        print('Mark got "Three of a kind"')

    if countsong == 1 :
        print('Mark got "Full House"')
       
else :
        print('Mark got "High Card"')
        
    
        