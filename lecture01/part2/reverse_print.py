# n = 1
# a = []
# while n !=  0 :
#     n = int(input())
#     a.append(n)
# len_a = - len(a) - 1
# i = -2
# while i > len_a :
#     print(a[i],end = ' ')
#     i -= 1

n = 1
a = []
while n !=  0 :
    n = int(input())
    a.append(n)

i = len(a) - 2

while i >= 0 :
    print(a[i])
    i -= 1
