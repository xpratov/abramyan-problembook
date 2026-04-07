n = int(input("N ni kiriting: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

if n < 2:
    print(0)
else:
    d = a[1] - a[0]
    is_arithmetic = True
    for i in range(1, n - 1):
        if a[i+1] - a[i] != d:
            is_arithmetic = False
            break
    if is_arithmetic:
        print(d)
    else:
        print(0)