def chartoint (arr):
	lenn = len(arr)
	newarr = list()
	for i in range(0,lenn) :
		newarr.append(int(arr[i]))
	return newarr

def mintomax(arr):
	lenn = len(arr)
	for i in range(0,lenn) :
		for j in range(i+1,lenn) :
			if(arr[i]>arr[j]) :
				arr[i],arr[j] = arr[j],arr[i]
	return arr

def cut(arr):
	lenn = len(arr)
	newarr = list()
	for i in range(0,lenn) :
		ch = 1
		for j in range(i+1,lenn) :
			if(arr[i]==arr[j]) :
				ch = 0
		if(ch==1) :
			newarr.append(arr[i])
	return newarr

num = input().split()
num = chartoint(num)
print(num)
num = mintomax(num)
print(num)
num = cut(num)
print(num)

for i in range (0,len(num),1):
	print(num[i],end=' ')