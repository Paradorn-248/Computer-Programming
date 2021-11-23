subject = int(input('How many subject: ')) 
total_credit = 0
list_grade = []
list_credit = []
sum_gxc = 0

def grade_to_num(grade) :
    if grade == 'A' :
        return 4
    elif grade == 'B+' :
        return 3.5
    elif grade == 'B' :
        return 3
    elif grade == 'C+' :
        return 2.5
    elif grade == 'C' :
        return 2
    elif grade == 'D+' :
        return 1.5
    elif grade == 'D' :
        return 1

for i in range(subject) :
    credit_get = float(input(f'Subject {i + 1} Credits: '))
    grade_get = input(f'Subject {i+1} Grade: ')
    list_credit.append(credit_get)
    list_grade.append(grade_get)
    total_credit += credit_get

for i in range(subject) :
    sum_gxc += list_credit[i] * grade_to_num(list_grade[i])

print(f'Output: Total Credit = {total_credit:.1f} ,GPA = {sum_gxc/total_credit:.2f}')
