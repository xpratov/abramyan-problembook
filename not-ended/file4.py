import os

count = 0

for _ in range(4):
    S = input()
    if os.path.exists(S):
        count += 1

print(count)