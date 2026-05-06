n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

for i in range(k):
  item = array.pop(0)
  array.append(item)

print(array)

