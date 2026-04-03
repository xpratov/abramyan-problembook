n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mn = min(numbers)
mx = max(numbers)

summa = 0
count = 0

for i in numbers:
  if i!=mn and i!=mx:
    summa+=i
    count+=1
print(summa/count)