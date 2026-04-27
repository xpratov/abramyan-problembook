n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

i = 0
while i < len(a):
    if a[i] % 2 != 0:
        val = a[i]
        a.insert(i + 1, val)
        a.insert(i + 1, val)
        i += 3 
    else:
        i += 1 

print(a)