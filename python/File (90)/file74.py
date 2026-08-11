I = int(input())
J = int(input())

with open("input.txt", "r") as f:
    numbers = list(map(float, f.read().split()))

n = int(len(numbers) ** 0.5)

if I > n or J > n:
    print(0.0)
else:
    index = (I - 1) * n + (J - 1)
    print(numbers[index])