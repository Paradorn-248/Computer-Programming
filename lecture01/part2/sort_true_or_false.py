numbers = []
for i in range(5) :
  n = int(input(f"Enter integer #0{i}: "))
  numbers.append(n)

a = sorted(numbers)
if a == numbers :
    print(True)

else :
    print(False)
