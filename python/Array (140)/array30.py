n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

biggers = []

for i in range(n-1):
  if numbers[i]>numbers[i+1]:
    biggers.append(i+1)

print(biggers, len(biggers))
