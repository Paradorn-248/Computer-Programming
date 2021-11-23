def union(set_a,set_b,union_list) :
    union_list.extend(set_a)
    for i in range(len(set_b)) :
        if set_b[i] not in union_list :
            union_list.append(set_b[i])

def empty_set(listt) :
    if len(listt) == 0 :
        listt.append('empty set')

def list_str_to_int(data,data_int) :
    for i in range(len(data)) :
        add = int(data[i])
        data_int.append(add) 

def present(listt) :
    string = str(listt[0])
    for i in range(1,len(listt)) :
        string += ', ' + str(listt[i])
    return string



set_a_str = input('Input set A: ').strip().split()
set_b_str = input('Input set B: ').strip().split()
set_a = []
set_b = []
list_str_to_int(set_a_str,set_a)
list_str_to_int(set_b_str,set_b)
# set_a = [2,3, 5, 7, 11, 13, 17, 19, 23]
# set_b = [3,5,7,9]

union_list = []


union(set_a,set_b,union_list)

empty_set(union_list)

union_list.sort()

if union_list[0] != 'empty set' :
    print(f'A union B: [{present(union_list)}]')
else :
    print(f'A union B: empty set')
