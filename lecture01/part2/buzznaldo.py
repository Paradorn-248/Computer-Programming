minute = int(input('How long have Buzz played ?: '))
hour = minute // 60
price = 0
if minute % 60 > 20 :
    hour += 1
if hour >= 2 and hour < 4 :
    price = hour * 900 * 9 // 10
elif hour == 4:
    price = hour * 900 *8 // 10
elif hour >= 5 :
    price = hour * 900 * 7 // 10
else :
    price = hour * 900


print(f'Total price is {price} baht.')