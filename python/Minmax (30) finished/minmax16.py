n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mn = min(numbers)
count = 0
for i in numbers:
  if i==mn:
    print(count)
    break
  count+=1
  
