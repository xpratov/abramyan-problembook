n = int(input("N ni kiriting: "))
a = list(map(int, input(f"{n} ta sondan iborat permutatsiyani kiriting: ").split()))

inversion_count = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inversion_count += 1

print(f"Inversiyalar soni: {inversion_count}")