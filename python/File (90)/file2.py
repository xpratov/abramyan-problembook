s = input("File nomini kiriting: ")
n = int(input("Butun son kiriting: "))

with open(s, "w") as f:
  for i in range(1, n+1):
    f.write(str(2*i) + "\n")