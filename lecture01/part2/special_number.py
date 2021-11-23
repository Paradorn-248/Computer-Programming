def checkcan(strings) :
	sum = 0
	for i in range(0,len(strings)) :
		sum += int(strings[i])**(i+1)
	if sum==int(strings) :
		return 'Y'
	return 'N'

arr = list()
strings = 'xxx'
while strings != '0' :
	strings = input("Input: ")
	arr.append(checkcan(strings))
for i in range(0,len(arr)-1) :
	print(arr[i],end='')