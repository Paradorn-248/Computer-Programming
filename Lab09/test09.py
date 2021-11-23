string_get = 1
a = 0
e = 0
i = 0
o = 0
u = 0
# print(string[2])
while string_get != '' :
	string_get = input('Enter message: ')
	# string = 'I love Python'
	string = string_get.lower()
	if string_get == '':
		print('Exiting the program.')
		exit()
	for z in range(len(string)) :
		if string[z] == 'a'  :
			a += 1
		if string[z] == 'e' :
			e += 1
		if string[z] == 'i' :
			i += 1
		if string[z] == 'o' :
			o += 1
		if string[z] == 'u' :
			u += 1
		# print(a,e,i,o,u)

	if a > 0:
		print(f'a: {a}')
	if e > 0:
		print(f'e: {e}')
	if i > 0:
		print(f'i: {i}')
	if o > 0:
		print(f'o: {o}')
	if u > 0:
		print(f'u: {u}')