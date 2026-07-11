def RootK(x, k, n):
    if n == 0:
        return 1.0

    y = RootK(x, k, n - 1)
    return y - (y - x / (y ** (k - 1))) / k


x = float(input("X ni kiriting: "))
k = int(input("K ni kiriting: "))
nlar = list(map(int, input("6 ta N ni kiriting: ").split()))

for n in nlar:
    print(f"N = {n}: {RootK(x, k, n):.6f}")