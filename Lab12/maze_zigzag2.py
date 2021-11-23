n =  int(input())
listt = [[0]*n for i in range(n)]
c = 0
a = 1
while True :   #ครึ่งแรก
    if c == n :
        break

    if c % 2 == 0 : #เคลื่อนขึ้น
        b = c
        for i in range(n-1,n-c-2,-1) :
            listt[i][b] = a
            b -= 1
            a += 1
        c += 1
        # print(c)
    else : #เคลื่อนลง
        b = 0
        for i in range(n-c-1,n) :
            listt[i][b] = a
            b += 1
            a += 1
        c += 1
        # print(c)
c = n-1
while True :#ครึ่งหลัง
    if c == 0 :
        break
    if c%2 == 0 :#เคลื่อนลง
        b = n-c
        for i in range(c) :
            listt[i][b] = a
            a += 1
            b += 1
        c -= 1
        # print(c)
    else :#เคลื่อนขึ้น
        b = n-1
        for i in range(c-1,-1,-1) :
            listt[i][b] = a
            a += 1
            b -= 1
        c -= 1
        # print(c)

for i in range(len(listt)):
    for j in range(len(listt[0])):
        print(f'{listt[i][j]:3.0f}',end=' ')
    print()

# print(listt)

