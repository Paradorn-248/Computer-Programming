def intersect(set_a,set_b,intersect_list) :
    len_a = len(set_a)
    for i in range(len_a) :
        if set_a[i] in set_b :
            intersect_list.append(set_a[i])

def union(set_a,set_b,union_list) :
    union_list.extend(set_a)
    for i in range(len(set_b)) :
        if set_b[i] not in union_list :
            union_list.append(set_b[i])

def a_minus_b(set_a,set_b,a_min_b_list) :
    a_min_b_list.extend(set_a)
    for i in range(len(set_b)) :
        if set_b[i] in a_min_b_list :
            a_min_b_list.remove(set_b[i])

def b_minus_a(set_a,set_b,b_min_a_list) :
    b_min_a_list.extend(set_b) 
    for i in range(len(set_a)) :
        if set_a[i] in b_min_a_list :
            b_min_a_list.remove(set_a[i])

def present(listt) :
    string = ''
    for i in range(len(listt)) :
        string += ' ' + str(listt[i])
    return string

def empty_set(listt) :
    if len(listt) == 0 :
        listt.append('empty set')

def list_str_to_int(data,data_int) :
    for i in range(len(data)) :
        add = int(data[i])
        data_int.append(add) 


set_a_str = input('Input setA: ').strip().split()
set_b_str = input('Input setB: ').strip().split()
set_a = []
set_b = []
list_str_to_int(set_a_str,set_a)
list_str_to_int(set_b_str,set_b)
# set_a = [2,3, 5, 7, 11, 13, 17, 19, 23]
# set_b = [3,5,7,9]
intersect_list = []
union_list = []
a_min_b_list = []
b_min_a_list = []
intersect(set_a,set_b,intersect_list)
union(set_a,set_b,union_list)
a_minus_b(set_a,set_b,a_min_b_list)
b_minus_a(set_a,set_b,b_min_a_list)
empty_set(intersect_list)
empty_set(b_min_a_list)
empty_set(a_min_b_list)
empty_set(union_list)
intersect_list.sort()
union_list.sort()
a_min_b_list.sort()
b_min_a_list.sort()

print(f'A intersect B:{present(intersect_list)}')
print(f'A minus B:{present(a_min_b_list)}')
print(f'B minus A:{present(b_min_a_list)}')
print(f'A union B:{present(union_list)}')
