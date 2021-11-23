text = 'stampstring'
print(text[1])

l = list(text)
# print(l)
l[1] = 'a' #error
a = str().join(l)
print(a)