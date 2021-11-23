a = int(input('Distance from starting point(m.): '))
sett = []
sum = 0
start = 0
count = 0
if a == 0 :
    print('0')
    print('Buzz moved 0 set(s)')
    exit()

while sum < a :
    sum += 5
    sett.append(sum)
    sum -= 2
    sett.append(sum)
    if sum == a:
        count += 1
        break
    count += 1


while sum > a :
    sum -= 4
    sett.append(sum)
    sum += 3
    sett.append(sum)
    if sum == a:
        count += 1
        break
    count += 1

for i in range(len(sett)) :
    print(str(sett[i]),end=(' '))
print()
print(f'Buzz moved {count} set(s)')