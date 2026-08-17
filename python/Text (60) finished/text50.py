import struct

with open("input.txt", "r") as f, \
     open("strings.bin", "wb") as strings, \
     open("numbers.bin", "wb") as numbers:

    for line in f:
        text = line[:30]
        number = float(line[30:].strip())

        strings.write(text.encode("utf-8"))
        numbers.write(struct.pack("d", number))