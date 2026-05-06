n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))
k = int(input("K ni kiriting (1 dan N gacha): "))
l = int(input("L ni kiriting (K dan N gacha): "))

sub_array = a[k-1 : l]
summa = sum(a)

result = (summa - sum(sub_array) ) / (len(a) - len(sub_array))

print(result)