sum=0
a=[]
while 1:
    n=input("Student's weight (or Enter to stop): ")
    if len(n)==0:
        break
    a.append(float(n))
a.sort()
cnt=0
for i in range(len(a)):
    sum+=a[i]
    if sum>200:
        sum=a[i]
        cnt+=1
    if i==len(a)-1:
        if sum!=0:
            cnt+=1
print(f"Elevator works {cnt} time(s).")

