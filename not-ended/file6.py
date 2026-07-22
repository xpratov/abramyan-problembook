import os

K = int(input())
S = input()

if not os.path.exists(S):
    print(-1)
else:
    with open(S, "r") as f:
        numbers = f.read().split()

    if 1 <= K <= len(numbers):
        print(numbers[K - 1])
    else:
        print(-1)