def Palindome(strings) :
	reverse = strings[::-1]
	if strings == reverse :
		return True
	return False

strings = input("Text: ")
a = len(strings)
lenn = a//2
sub1 = strings[lenn:]
sub2 = strings[:lenn]
if a%2 == 1 : 
	sub1 = sub1[1:]
	# print(sub1)
x = Palindome(strings.upper())
y = Palindome(sub1.upper())
z = Palindome(sub2.upper())
if x and y and z : print("Double Palindrome")
elif x : print("Palindrome")
else : print("No")