import os
import struct

def InvIntFile(S):
    if not os.path.exists(S):
        return

    nums = []

    with open(S, "rb") as f:
        while True:
            data = f.read(4)
            if not data:
                break
            nums.append(struct.unpack("i", data)[0])

    nums.reverse()

    with open(S, "wb") as f:
        for x in nums:
            f.write(struct.pack("i", x))


for _ in range(3):
    name = input()
    InvIntFile(name)