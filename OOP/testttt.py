s = input('Enter a string, such as "ILoveYou" : ')
for i in range(len(s)+1):
    for j in range(len(s)-i):
        print(" ",end=" ")
    for j in range(0,i,1):
        print(s[j],"",end="")
    for j in range(i,1,-1):
        print(s[j-2], "", end="")
    print()
for i in range(len(s)):
    for j in range(0, i+1, 1):
        print(" ", end=" ")
    for j in range(0,len(s)-i-1,1):
        print(s[j],"", end="")
    for j in range(len(s)-i-3,-1,-1):
        print(s[j],"", end="")
    print("")
