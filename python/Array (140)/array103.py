n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

mininx = a.index(min(numbers))
maxinx = a.index(max(numbers))

if mininx<maxinx:
  numbers.insert(maxinx+1, 0.0)
  numbers.insert(mininx, 0.0)
else:
  numbers.insert(mininx, 0.0)
  numbers.insert(maxinx+1, 0.0)

print(numbers)