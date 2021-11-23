import math
a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))
d = int(input('Input d: '))
e = int(input('Input e: '))

mean = (a+b+c+d+e) / 5

sd = math.sqrt((((mean-a)**2)+((mean-b)**2)+((mean-c)**2)+((mean-d)**2)+((mean-e)**2))/5)

print(f'mean: {mean:.3f}')
print(f'sd: {sd:.3f}')