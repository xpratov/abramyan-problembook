import os

def LineCount(S):
    if not os.path.exists(S):
        return -1

    with open(S, "r") as f:
        return sum(1 for _ in f)


for _ in range(3):
    name = input()
    print(LineCount(name))