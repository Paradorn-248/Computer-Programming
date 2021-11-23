data = input().strip().split()
alpha = []
number = []
special = []

for i in range(len(data)) :
    if ord(data[i]) in range(97,123) or ord(data[i]) in range(65,91) :
        alpha.append(data[i])
    elif ord(data[i]) in range(48,58) :
        number.append(data[i])
    else  :
        special.append(data[i])
        
print('Alphabet: ' + str(alpha))
print('Number: ' + str(number))
print('Special: ' + str(special))
