n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))
k = int(input(f"K ni kiriting (1 dan {n} gacha): "))

initial_ak = a[k-1]

for i in range(n):
    a[i] += initial_ak

print("Natija:")
print(a)