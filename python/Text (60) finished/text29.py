filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

words = text.split()

max_word = words[0]

for word in words:
    if len(word) > len(max_word):
        max_word = word

print(max_word)