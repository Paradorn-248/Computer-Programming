a = input('Input a: ')
b = input('Input b: ')
c = input('Input c: ')

aa = float(a)
bb = float(b)
cc = float(c)

if aa > bb and aa > cc :
    print(f'Maximum is {a}')
if bb > aa and bb > cc :
    print(f'Maximum is {b}')
if cc > bb and cc > aa :
    print(f'Maximum is {c}')