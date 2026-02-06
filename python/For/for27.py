x = float(input("X - haqiqiy son (|X|<1)ni kiriting: "))
n = int(input("N - butun son (>0)ni kiriting: "))

summa = 0

for k in range(n + 1):
    numerator = 1
    for j in range(1, 2*k, 2):
        numerator *= j
    denominator = 1
    for j in range(1, k+1):
        denominator *= 2*j
    denominator *= (2*k + 1)
    summa += numerator * (x**(2*k + 1)) / denominator

print(summa)
