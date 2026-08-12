s = input("File nomini kiriting: ")

with open(s, "r") as f:
  numbers = f.read().split()
  n = len(numbers)
  print(numbers[0])
  print(numbers[1])
  print(numbers[n-2])
  print(numbers[n-1])
