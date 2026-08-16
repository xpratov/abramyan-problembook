filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

words = text.split()

min_word = words[-1]

for word in reversed(words):
    if len(word) < len(min_word):
        min_word = word

print(min_word)