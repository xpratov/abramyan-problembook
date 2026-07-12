K = int(input())
N = int(input())

result = True

for i in range(N):
    number = int(input())
    if number < K:
        result = False
        break

print(result)