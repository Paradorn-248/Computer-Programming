def fac(n) :
    sum = 1
    for i in range(1,n+1) :
        sum *= i 
    return sum
# หาเลข0หลังค่าfac()
# n = 100
# res = fac(n)
# len_sum = len(str(res))
# nub = 0
# for i in range(len_sum,-1,-1) :
#     if res % 10 == 0 :
#         nub += 1
#         res //= 10
#     else :
#         break
# print(nub)

# หาค่าe
n = 100
sum = 2
for i in range(2,n) :
    sum+= 1/fac(i)
print(sum)