n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

indices_to_zero = []

for i in range(n):
    if i == 0:
        if n > 1 and a[i] > a[i+1]:
            indices_to_zero.append(i)
    elif i == n - 1:
        if a[i] > a[i-1]:
            indices_to_zero.append(i)
    else:
        if a[i] > a[i-1] and a[i] > a[i+1]:
            indices_to_zero.append(i)

for idx in indices_to_zero:
    a[idx] = 0

print("Natija:", a)