s = input("Matn kiriting: ")

punctuations = ".,!?;:-()\"'"

for punc in punctuations:
  s = s.replace(punc, " ")

words = s.split()

longest = words[0]

for word in words:
  if len(word)>len(longest):
    longest = word

print(longest)