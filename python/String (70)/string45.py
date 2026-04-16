s = input("Matn kiriting: ")

words = s.split()
less = len(words[0])

for word in words:
  if len(word)<less:
    less = len(word)

print(less)