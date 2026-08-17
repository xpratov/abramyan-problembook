import struct

with open("input.txt", "r") as f, \
     open("column1.bin", "wb") as f1, \
     open("column2.bin", "wb") as f2, \
     open("column3.bin", "wb") as f3:

    for line in f:
        numbers = line.split()

        f1.write(struct.pack("d", float(numbers[0])))
        f2.write(struct.pack("d", float(numbers[1])))
        f3.write(struct.pack("d", float(numbers[2])))