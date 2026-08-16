import struct

C = input("C = ")
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

words = []
word = ""

for ch in text:
    if ch.isalpha():
        word += ch
    else:
        if word and C.lower() in word.lower():
            words.append(word)
        word = ""

if word and C.lower() in word.lower():
    words.append(word)

with open("result.bin", "wb") as f:
    for word in words:
        data = word.encode()
        f.write(struct.pack("I", len(data)))
        f.write(data)