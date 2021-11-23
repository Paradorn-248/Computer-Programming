
n = 14
def num(n) :
    listt = []
    if n %2 != 0 : 
        for i in range(1,n//2+1) :
            add = 2*i**2+i
            listt.append(add)
            listt.append(add+1)

    else :
        for i in range(1,n//2+1) :
            add = 2*i**2+i
            listt.append(add)
            listt.append(add+1)
        listt = listt[:-1]
# print(listt)
for i in range(n) :
    