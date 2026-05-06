n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

min_idx = 0
max_idx = 0

for i in range(1, n):
    if a[i] < a[min_idx]:
        min_idx = i
    if a[i] > a[max_idx]:
        max_idx = i

a[min_idx], a[max_idx] = a[max_idx], a[min_idx]

print("Natija:")
print(a)