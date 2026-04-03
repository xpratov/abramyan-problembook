n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

odds = [i for i in numbers if i%2!=0]
max_odd = max(odds)

count = 1
for i in numbers:
  if max_odd == i:
    print(count)
    break
  count+=1
