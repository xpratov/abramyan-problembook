x = float(input("X - haqiqiy son (|X|<1)ni kiriting: "))
n = int(input("N - butun son (>0)ni kiriting: "))

summa = 1

for k in range(1, n+1):
    numerator = 1
    for j in range(1, 2*k-1, 2):
        numerator *= j
    denominator = 1
    for j in range(2, 2*k+1, 2):
        denominator *= j
    summa += ((-1)**(k-1)) * (numerator * (x**k) / denominator)

print(summa)