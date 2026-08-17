import struct

with open("input.txt", "r") as f:
    lines = f.readlines()

with open("numbers.bin", "rb") as f:
    numbers = []

    while True:
        data = f.read(4)

        if not data:
            break

        numbers.append(struct.unpack("i", data)[0])

with open("result.txt", "w") as f:
    for i in range(len(lines)):
        line = lines[i].rstrip("\n")

        if i < len(numbers):
            line += str(numbers[i])

        f.write(line + "\n")