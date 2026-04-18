s = input("Matn kiriting: ")

words = s.split()
results = []

for word in words:
  word = word[0].upper() + word[1:]
  results.append(word)


print(" ".join(results))