r = int(input('R: '))
c = int(input('C: '))

sum = 0
for i in range(1,min(r,c)+1) :
    sum += (r-(i-1))*(c-i+1)

print(sum)