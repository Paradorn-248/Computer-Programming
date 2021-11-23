def setwater(numbers,arrays) :
	arrays.append(numbers) 
	for i in range(0,100) :
		sum = 0
		for j in range(0,len(arrays[i])) :
			sum += int(arrays[i][j])
		arrays.append(str(int(arrays[i])+sum))

def oh_water(numbers) :
	ans = list()
	while True :
		if numbers in arr1 :
			ans.append('1')
			ans.append(numbers)
		if numbers in arr3 :
			ans.append('3')
			ans.append(numbers)
		if numbers in arr9 :
			ans.append('9')
			ans.append(numbers)
		if len(ans) != 0 :
			break
		sum = 0
		for j in range(0,len(numbers)) :
			sum += int(numbers[j])
		numbers = str(int(numbers)+sum)
	return ans


arr1,arr3,arr9 = list(),list(),list()
setwater('1',arr1)
setwater('3',arr1)
setwater('9',arr1)

N = input("N: ")
ans = oh_water(N)
for i in range(0,len(ans)//2) :
	print(ans[2*i]+' '+ans[2*i+1])