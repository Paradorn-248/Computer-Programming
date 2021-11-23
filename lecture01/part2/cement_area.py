w = int(input('w: '))
h = int(input('h: '))
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

area = w*h - (a*(b+c)) - (a * (b + c))

print('Area: {:.2f}'.format(area))