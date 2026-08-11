import struct


def TextToStringFile(S):
    with open(S, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(S, "wb") as f:
        for line in lines:
            text = line.rstrip("\n")
            data = text.encode()

            f.write(struct.pack("i", len(data)))
            f.write(data)


S1 = input()
S2 = input()

TextToStringFile(S1)
TextToStringFile(S2)