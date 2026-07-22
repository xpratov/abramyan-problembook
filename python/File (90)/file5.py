import os

s = input("file nomini kiriting: ")

if not os.path.exists(s):
  print(-1)
else:
  with open(s, "r") as f:
    numbers = f.read().split()
  print(len(numbers))