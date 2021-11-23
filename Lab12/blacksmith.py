def grade_cal(data) :
    per_25 = (n**2)//4 
    #หาจำนวนแต่ละเปอร์เซ็น
    more85,more70,more90= 0,0,0
    for i in range(n) :
        for j in range(n) :
            if data[i][j] >= 90 :
                more90 += 1
            if data[i][j] >= 85 :
                more85 += 1
            if data[i][j] >= 70 :
                more70 += 1

    #คิดบวกแต่ละช่อง
    res = []
    for i in range(n-2) :
        for j in range(n-2) :        
            sum = data[i][j] + data[i+1][j] + data[i+2][j]+data[i][j+1] + data[i+1][j+1] + data[i+2][j+1]+data[i][j+2] + data[i+1][j+2] + data[i+2][j+2]
            res.append(sum/9)
    # print(res)
    
    # Grade C (Upgrade From No Grade)
    avr_85,avr_70,avr_60,nog =0,0,0,0
    for i in res :
        if i >= 85 :
            avr_85 += 1
        if i >= 70 :
            avr_70 += 1
        if i >= 60 :
            avr_60 += 1
        if i < 60 :
            nog += 1

    #คัดเกรด
    # print(res)
    # print(avr_85,avr_70,avr_60,nog)
    if avr_85 == len(res) :
        return 'Grade A'
    if avr_70 == len(res) and more90 > per_25 :
        return 'Grade A (Upgrade From B)'
    if avr_70 == len(res) :
        return 'Grade B'
    if avr_60 == len(res) and more85 > per_25:
        return 'Grade B (Upgrade From C)'
    if avr_60 == len(res):
        return 'Grade C'
    if nog > 0 and more70 > per_25 :
        return 'Grade C (Upgrade From No Grade)'
    if nog > 0:
        return 'No Grade'
        
        
n = int(input('Material size: '))
# n = 5
mat = []
for i in range(n) :
    add = input().strip().split()
    for j in range(n) :
        add[j] = int(add[j])
    mat.append(add)

print(f'Output: {grade_cal(mat)}')
