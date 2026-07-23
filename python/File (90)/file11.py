s = input("Haqiqiy sonlardan iborat faylning nomini kiriting: ")
even_file = input("Juft tartibli sonlar yoziladigan fayl nomini kiriting: ")
odd_file = input("Toq tartibli sonlar yoziladigan fayl nomini kiriting: ")

with open(s, "r") as f:
  numbers = f.read().split()

with open(even_file, "x") as f:
  for i in range(1, len(numbers), 2):
    f.write(numbers[i] + "\n")

with open(odd_file, "x") as f:
  for i in range(0, len(numbers), 2):
    f.write(numbers[i] + "\n")

