s1 = input("1-fayl nomini yozing: ")
s2 = input("2-fayl nomini yozing: ")

with open(s1, "r") as f:
  components = f.read().split()

with open(s2, "x") as f:
  f.write(components[0] +"\n")
  f.write(components[-1])

