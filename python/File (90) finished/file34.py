s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
  components = f.read().split()

positives = [x for x in components if x>0]

with open(s, "w") as f:
  f.write(" ".join(positives))