s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
  summa = 0
  numbers = f.read().split()
  for i in range(2, len(numbers), 2):
    summa += float(numbers[i])

print(summa)
