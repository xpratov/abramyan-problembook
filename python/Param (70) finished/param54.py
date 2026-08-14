def SplitText(S0, K, S1, S2):
    with open(S0, "r") as f:
        lines = f.readlines()

    with open(S1, "w") as f:
        f.writelines(lines[:K])

    with open(S2, "w") as f:
        f.writelines(lines[K:])


S0 = input()
K = int(input())
S1 = input()
S2 = input()

SplitText(S0, K, S1, S2)