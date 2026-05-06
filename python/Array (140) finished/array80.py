n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

for i in range(n - 1):
    a[i] = a[i + 1]

if n > 0:
    a[n - 1] = 0

print("Natija:", a)