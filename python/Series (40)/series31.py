k = int(input())
n = int(input())

count = 0

for i in range(k):
    a = list(map(int, input().split()))

    if 2 in a:
        count += 1

print(count)