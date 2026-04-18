s = input("Matn kiriting:")

words = s.split()
modifies = []

for word in words:
  first = word[0]
  modified = first + word[1:].replace(first, ".")
  modifies.append(modified)

print(" ".join(modifies))