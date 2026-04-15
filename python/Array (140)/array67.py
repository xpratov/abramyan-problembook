n = int(input("N - butun sonini kiriting: "))
array = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

odd = None
for el in array:
  if el%2==1:
    odd = el

if odd is None:
  print(array)
else:
  for i, val in enumerate(array):
    if val%2==1:
      array[i] += odd
  print(array)
