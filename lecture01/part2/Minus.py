def minus(set_a,set_b) :
    a_min_b_list.extend(set_a)
    for i in range(len(set_b)) :
        if set_b[i] in a_min_b_list :
            a_min_b_list.remove(set_b[i])
    return a_min_b_list
            
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

a_min_b_list = []


minus(set_a,set_b)

empty_set(a_min_b_list)

a_min_b_list.sort()

if a_min_b_list[0] != 'empty set' :
    print(f'A minus B: [{present(a_min_b_list)}]')
else :
    print(f'A minus B: empty set')
