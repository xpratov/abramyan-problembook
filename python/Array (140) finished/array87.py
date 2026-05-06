n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

first = array.pop(0)
placed = False

for i in range(len(array)):
  if array[i]>first:
    array.insert(i, first)
    placed = True
    break

if not placed:
  array.append(first)
print(array)


