import math as m

def IsSquare(k):
  root = m.sqrt(k)
  if root == int(root):
    return True
  return False

k = int(input("K - musbat butun son kiriting: "))

numbers = [4, 10, 16, 25, 30, 49, 50, 64, 81, 100]

count = 0
for s in numbers:
    if IsSquare(s):
        count += 1

print(f"Ketma-ketlikdagi kvadrat sonlar soni: {count}")

