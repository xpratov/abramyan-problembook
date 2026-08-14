def AddLineNumbers(S, N, K, L):
    with open(S, "r") as f:
        lines = f.readlines()

    with open(S, "w") as f:
        for i, line in enumerate(lines):
            text = line.rstrip("\n")

            number = str(N + i).rjust(K)

            if text:
                f.write(number + " " * L + text + "\n")
            else:
                f.write(number.rstrip() + "\n")


S = input()
N = int(input())
K = int(input())
L = int(input())

AddLineNumbers(S, N, K, L)