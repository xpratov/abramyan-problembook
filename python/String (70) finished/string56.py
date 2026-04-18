s = input("Matn kiriting: ")

punctuations = ".,!?;:-()\"'"

for punc in punctuations:
  s = s.replace(punc, " ")

words = s.split()

shortest = words[0]

for word in words:
  if len(word)<=len(shortest):
    shortest = word

print(shortest)