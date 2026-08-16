import struct
import string

K = int(input("K = "))
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

words = []
word = ""

for ch in text:
    if ch.isalnum():
        word += ch
    else:
        if len(word) == K:
            words.append(word)
        word = ""

if len(word) == K:
    words.append(word)

with open("result.bin", "wb") as f:
    for word in words:
        data = word.encode()
        f.write(struct.pack("I", len(data)))
        f.write(data)