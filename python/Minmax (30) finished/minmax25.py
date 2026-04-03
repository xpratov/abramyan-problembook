n = int(input("N (N > 2): "))
numbers = list(map(float, input(f"{n} ta son kiriting: ").split()))

min_prod = numbers[0] * numbers[1]
inx = 1

for i in range(1, n-1):
  current_prod = numbers[i] * numbers[i+1]
  if current_prod < min_prod:
    min_prod = current_prod
    inx = i+1

print(inx, inx+1)
