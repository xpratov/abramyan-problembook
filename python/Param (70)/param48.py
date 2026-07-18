import os
import struct

def IntFileSize(S):
    if not os.path.exists(S):
        return -1

    return os.path.getsize(S) // struct.calcsize("i")


for _ in range(3):
    name = input()
    print(IntFileSize(name))