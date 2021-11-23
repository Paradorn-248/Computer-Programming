password_get = input()
len_pass = len(password_get)
password = int(password_get)
pass_list = []
for i in range(len_pass) :
    add = int(password_get[i])
    pass_list.append(add)

# print(pass_list)
count = 0
i = 0

while count < len_pass :
    hacker_get = int(input())
    if hacker_get == pass_list[i] and count < len_pass:
        count += 1
        i += 1 
    
    else :
        break

if count == len_pass :
    print('Succeed!!')
else :
    print('Fail!!')
