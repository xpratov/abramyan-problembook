import struct


def SplitIntFile(S0, K, S1, S2):
    with open(S0, "rb") as f:
        data = f.read()

    numbers = []

    for i in range(0, len(data), 4):
        numbers.append(struct.unpack("i", data[i:i + 4])[0])

    with open(S1, "wb") as f:
        for number in numbers[:K]:
            f.write(struct.pack("i", number))

    with open(S2, "wb") as f:
        for number in numbers[K:]:
            f.write(struct.pack("i", number))


S0 = input()
K = int(input())
S1 = input()
S2 = input()

SplitIntFile(S0, K, S1, S2)