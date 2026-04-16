s = input("Matn kiriting: ")

words = s.split()
longest = len(words[0])

for word in words:
  if len(word)>longest:
    longest = len(word)

print(longest)