N = int(input())

sonlar = []
for _ in range(N):
    sonlar.append(int(input()))

K = 0

for i in range(N - 1):
    if sonlar[i] < sonlar[i + 1]:
        print(sonlar[i])
        K += 1

print("K =", K)