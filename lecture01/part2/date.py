d = int(input('d: '))
m = int(input('m: '))
y = int(input('y: '))

day_in_month = ['',31,28,31,30,31,30,31,31,30,31,30,31]    
date = 0

def leap_year(y) :
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

if leap_year(y) == True :
    day_in_month[2] = 29

for i in range(1,m) :
    date += day_in_month[i]

date = date + d

print(date)

