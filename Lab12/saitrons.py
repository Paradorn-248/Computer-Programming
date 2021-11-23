def direction(plate,before) :
    if plate == '\\' :    
        if before == 'up' :
            direct = 'left' 
        if before =='down' :
            direct = 'right' 
        if before == 'left' :
            direct = 'up' 
        if before == 'right' :
            direct = 'down' 
    if plate == '/' :
        if before == 'up' :
            direct = 'right' 
        if before =='down' :
            direct = 'left' 
        if before == 'left' :
            direct = 'down' 
        if before == 'right' :
            direct = 'up' 
    return direct
    
def max_saitron(field) :
    res = []
    for i in range(len(field)) :
        before = 'right'
        j = 0
        sum_up = 0
        while True :
            if field[i][j] == '/' or field[i][j] == '\\' :
                before = direction(field[i][j],before)
                sum_up += 1
            if (before == 'up' and i == 0) or (before == 'down' and i == len(field)-1) or (before == 'left' and j == 0) or (before == 'right' and j == len(field[i])-1):
                break
            if before == 'up' :
                i -= 1
            if before == 'down' :
                i += 1
            if before == 'left' :
                j -= 1
            if before == 'right' :
                j += 1
        res.append(2**sum_up)
    for i in range(len(field)) :
        before = 'left'
        j = len(field[i]) - 1
        sum_up = 0
        while True :
            if field[i][j] == '/' or field[i][j] == '\\' :
                before = direction(field[i][j],before)
                sum_up += 1
            if (before == 'up' and i == 0) or (before == 'down' and i == len(field)-1) or (before == 'left' and j == 0) or (before == 'right' and j == len(field[i])-1):
                break
            if before == 'up' :
                i -= 1
            if before == 'down' :
                i += 1
            if before == 'left' :
                j -= 1
            if before == 'right' :
                j += 1
        res.append(2**sum_up)
    for j in range(len(field[0])) :
        before = 'up'
        i = len(field) - 1    
        sum_up= 0
        while True :
            if field[i][j] == '/' or field[i][j] == '\\' :
                before = direction(field[i][j],before)
                sum_up += 1
            if (before == 'up' and i == 0) or (before == 'down' and i == len(field)-1) or (before == 'left' and j == 0) or (before == 'right' and j == len(field[i])-1):
                break
            if before == 'up' :
                i -= 1
            if before == 'down' :
                i += 1
            if before == 'left' :
                j -= 1
            if before == 'right' :
                j += 1
        res.append(2**sum_up)
    for j in range(len(field[0])) :
        before = 'down'
        i = 0
        sum_up = 0
        while True :
            if field[i][j] == '/' or field[i][j] == '\\' :
                before = direction(field[i][j],before)
                sum_up += 1
            if (before == 'up' and i == 0) or (before == 'down' and i == len(field)-1) or (before == 'left' and j == 0) or (before == 'right' and j == len(field[i])-1):
                break
            if before == 'up' :
                i -= 1
            if before == 'down' :
                i += 1
            if before == 'left' :
                j -= 1
            if before == 'right' :
                j += 1
        res.append(2**sum_up)
    
    # print(res)
    return max(res)


# field = [['/','\\','\\','o','/','/','o'],['o','\\','/','o','\\','o','\\'],['o','o','o','o','o','o','o'],['o','o','o','o','o','o','o'],['\\','o','\\','o','o','o','o'],['o','o','o','o','o','/','/'],['o','o','o','o','o','/','o'],['o','o','o','o','o','o','o']]
field = []
add = 1
while True :
    add = input().strip().split()
    if add != [] :
        field.append(add)
    else :
        break
    
print(f'Maximum saitron is {max_saitron(field)} particle(s)')