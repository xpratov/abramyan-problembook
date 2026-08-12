S1 = input()
S2 = input()

with open(S1, "r") as f:
    numbers = f.read().split()

with open(S2, "x") as f:
    for num in reversed(numbers):
        f.write(num + "\n")