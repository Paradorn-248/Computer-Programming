def draw(m):
	arr = m
	lenn = len(arr)
	for i in range(0,lenn) :
		for _ in range(0,i+1) :
			print(arr[i],end='')
		print()

arr = list()
while True :
	arr = input().split()
	if len(arr)==1 and arr[0] == '0' :
		print("Good Bye.")
		break
	draw(arr)