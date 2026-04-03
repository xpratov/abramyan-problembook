n = int(input("N (N > 2): "))
numbers = list(map(float, input(f"{n} ta son kiriting: ").split()))

max_summa = numbers[0]+numbers[1]

for i in range(1, n-1):
  current_summa = numbers[i] + numbers[i+1]
  if max_summa < current_summa:
    max_summa = current_summa

print(max_summa)