n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mx = numbers[0]
count = 0
for i in numbers:
  if i>=mx:
    mx=i
    count=0
  else:
    count+=1
print(count)
  
