def par_to_score(par) :
    if par == 'Ea' :
        return -2
    elif par == 'Bi' :
        return -1
    elif par == 'Pa' :
        return 0
    elif par == 'Bo' :
        return 1
    elif par == 'DB' :
        return 2

par = []
hit = []
sum = 0

par = input().strip().split()

hit = input().strip().split()

for i in range(9) :
    sum += int(par[i]) + par_to_score(hit[i]) 

print(sum)