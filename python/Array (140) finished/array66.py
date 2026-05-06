n = int(input("N - butun sonini kiriting: "))
array = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

even = None
for el in array:
  if el%2==0:
    even = el
    break
if even is None:
  print(array)
else:
  for i in range(len(array)):
    if array[i]%2==0:
      array[i] += even
  print(array)
