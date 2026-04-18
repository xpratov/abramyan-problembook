s = input("Matn kiriting:")

words = s.split()
modifies = []

for word in words:
  last = word[-1]
  modified = word[:-1].replace(last, ".") + last
  modifies.append(modified)

print(" ".join(modifies))