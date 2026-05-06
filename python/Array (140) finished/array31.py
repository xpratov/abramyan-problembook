n = int(input("N - butun sonini kiriting: "))
floats = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

orders = []

for i in range(1, len(floats)):
  if floats[i] < floats[i-1]:
    orders.append(i+1)

orders.reverse()
print(orders, len(orders))