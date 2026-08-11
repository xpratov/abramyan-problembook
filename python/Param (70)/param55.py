import struct


def StringFileToText(S):
    with open(S, "rb") as f:
        strings = []

        while True:
            data = f.read(4)

            if not data:
                break

            length = struct.unpack("i", data)[0]

            text = f.read(length).decode()

            strings.append(text)

    with open(S, "w", encoding="utf-8") as f:
        for text in strings:
            f.write(text + "\n")


S1 = input()
S2 = input()

StringFileToText(S1)
StringFileToText(S2)