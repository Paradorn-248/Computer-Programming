def mod(N,M):
	arr = list()
	for i in range(0,N) :
		num = int(input("Input number %d: "%(i+1)))
		if num%M in arr :
			continue
		arr.append(num%M)
	return arr

N = int(input("N: "))
M = int(input("M: "))
arr =  mod(N,M)
print(len(arr))