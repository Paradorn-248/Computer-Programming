lis = []
c= 0
savesave = 0
savenub = 0
nub = 1
save = 0
while True:
	a = int(input())
	if a==0 : 
		break
	if c==0 :
		savesave = a
		savenub = 1
		c = 1
	lis.append(a)
	if len(lis)>1 :
		if(lis[len(lis)-1]==lis[len(lis)-2]) :
			save = a
			nub += 1
			if nub>savenub :
				savesave = save
				savenub = nub
		else :
			save = 0
			nub = 1

print(savenub)
print(savesave)