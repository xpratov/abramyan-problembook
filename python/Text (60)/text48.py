import struct

with open("input.txt", "r") as f, \
     open("result.bin", "wb") as out:

    for line in f:
        numbers = line.split()

        for item in numbers:
            x = float(item)

            if x.is_integer():
                out.write(struct.pack("i", int(x)))