x = int(input('x: '))
op = input('Operator: ')
y = int(input('y: '))

if op == '+':
    print(x + y)

elif op == '-':
    print(x - y)

elif op == '*':
    print(x * y)

elif op == '/':
    print('{:.2f}'.format(x / y))

elif op == '%':
    print(x % y)

else :
    print('Unknown Operator')