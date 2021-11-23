def findmax(a,n,m):
	lena = len(a)
	maxx = list()
	name = list()
	sum = [0] * n
	for i in range(0,lena) :
		minn = 1e9
		for j in range(1,len(a[i])) :
			sum[i] += int(a[i][j])
			minn = min(int(a[i][j]),minn)
		sum[i] = sum[i] - minn
		maxx.append(sum[i])
	maxi = max(maxx)
	for i in range(0,lena) :
		if sum[i] == maxi :
			name.append(a[i][0])
	return maxi,name


def printans(maxi,name):
	print(maxi)
	for i in range(0,len(name)) :
		print(name[i])

n = int(input("n = "))
m = int(input("m = "))
a = []
for i in range (0,n,1):
	k = input().split()
	a.append(k)

maxi,name = findmax(a,n,m)
printans(maxi,name)