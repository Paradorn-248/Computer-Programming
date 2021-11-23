def leap_year(year) :
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

eachmonth = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]    
sumday = 0
sumsecond = 0

print('Unix Time Converter')
day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

#check day input
if day < 0 or month < 0 or year < 1970 :
    print(f'Error: {day:02d}/{month:02d}/{year} does not exist!')
    exit() 
if month in [1,3,5,7,8,10,12] and day > 31:
    print(f'Error: {day:02d}/{month:02d}/{year} does not exist!')
    exit() 
if month in [4,6,9,11] and day > 30:
    print(f'Error: {day:02d}/{month:02d}/{year} does not exist!')    
    exit() 
if month == 2 and leap_year(year) == True and day > 29:
    print(f'Error: {day:02d}/{month:02d}/{year} does not exist!') 
    exit()  
if month == 2 and leap_year(year) == False and day > 28:
    print(f'Error: {day:02d}/{month:02d}/{year} does not exist!')
    exit()  
    
hour = int(input('Hour: '))
minute = int(input('Minute: '))
second = int(input('Second: '))
#check time input
if hour not in range(0,24) or minute not in range(0,60) or second not in range(0,60) :
    print(f'Error: {hour:02d}:{minute:02d}:{second:02d} does not exist!') 
    exit() 

#calculate year
for i in range(year - 1970) :
    if leap_year(i) == True :
        day_in_year = 366
    else :
        day_in_year = 365
    sumday += day_in_year 

        
#calculate day
if leap_year(year) == True :
    day_in_month[1] = 29
    for i in range(1,month) :
        sumday += day_in_month[i]
    sumday += day 

else :
    for i in range(1,month) :
        sumday += day_in_month[i]
    sumday += day 

sumday -= 1
sumsecond += sumday * 24 * 3600
#sum hour
sumsecond += hour * 3600
#sum minute
sumsecond += minute * 60
#sum second
sumsecond += second

print(sumday)
print(f'{day:02d}/{eachmonth[month-1]}/{year} @ {hour:02d}:{minute:02d}:{second:02d} is {sumsecond} seconds from 01/Jan/1970')


