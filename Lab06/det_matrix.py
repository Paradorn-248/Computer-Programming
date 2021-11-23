matt = []
for i in range(3) :
    n = input(f'Row {i+1} : ').split()
    for j in range(3) :
        n[j] = int(n[j])
    matt.append(n)
print(matt)
sumlower = (matt[0][0]*matt[1][1]*matt[2][2]) + (matt[0][1]*matt[1][2]*matt[2][0]) + (matt[0][2]*matt[1][0]*matt[2][1])
sumupper = (matt[2][0]*matt[1][1]*matt[0][2]) + (matt[2][1]*matt[1][2]*matt[0][0]) + (matt[2][2]*matt[1][0]*matt[0][1])
print(sumlower-sumupper)