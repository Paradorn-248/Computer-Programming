savenum = 0
savenub = 0
num = 0
nub = 1
lis = []
check = 0

while True :
    a = int(input())
    if a == 0 :
        break

    if check == 0 :
        savenum = a
        savenub = 1
        check = 1

    lis.append(a)

    if len(lis) > 1 :
        if lis[len(lis)-1] == lis[len(lis)-2] :
            num = a
            nub += 1
            if nub > savenub :
                savenub = nub
                savenum = num
        
        else :
            nub = 1
            num = 0

print(savenub)
print(savenum)

        