n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mn = min(numbers)
mx = max(numbers)

count = 1
for i in numbers:
  if i==mn or i==mx:
    print(count)
    break
  count+=1