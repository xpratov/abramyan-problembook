n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mn = min(numbers)

count = 0
longest = 0

for i in numbers:
  if i==mn:
    count+=1
  else:
    if longest<count:
      longest = count
    count = 0

if count > longest:
  longest = count
print(longest)