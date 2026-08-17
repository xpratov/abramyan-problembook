import struct

separator = input("Separator: ")

with open("input.txt", "r") as f, \
     open("result.bin", "wb") as out:

    for line in f:
        parts = line.strip().split(separator)

        a = float(parts[1])
        b = float(parts[2])
        c = float(parts[3])

        total = int(a + b + c)

        out.write(struct.pack("i", total))