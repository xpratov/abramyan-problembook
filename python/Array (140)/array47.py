n = int(input("N - butun sonini kiriting: "))
integers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

print(len(list(set(integers))))