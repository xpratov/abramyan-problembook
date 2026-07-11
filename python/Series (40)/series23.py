n = int(input("N - butun sonini kiriting: "))
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

result = 0

for i in range(1, n - 1):
    if not (
        (nlar[i] > nlar[i - 1] and nlar[i] > nlar[i + 1]) or
        (nlar[i] < nlar[i - 1] and nlar[i] < nlar[i + 1])
    ):
        result = i + 1
        break

print(result)