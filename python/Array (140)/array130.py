n = int(input("N ni kiriting: "))
numbers = list(map(int, input(f"{n} ta son kiriting: ").split()))

values = []  
lengths = [] 

if n>0:
  current_val = numbers[0]
  count = 1
  for i in range(1, n):
    if numbers[i] == current_val:
      count += 1
    else:
      values.append(current_val)
      lengths.append(count)
      current_val = numbers[i]
      count = 1
  values.append(current_val)
  lengths.append(count)

max_len = max(lengths)

for i in range(len(lengths)):
    if lengths[i] == max_len:
      lengths[i] += 1


result = []
for i in range(len(lengths)):
  result.extend([values[i]] * lengths[i])

print(result)