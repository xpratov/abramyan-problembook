n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

original_a = list(a)

for i in range(n):
    if i == 0:
        if n > 1:
            a[i] = (original_a[i] + original_a[i+1]) / 2
    elif i == n - 1:
        a[i] = (original_a[i] + original_a[i-1]) / 2
    else:
        a[i] = (original_a[i-1] + original_a[i] + original_a[i+1]) / 3

print("Natija:", a)