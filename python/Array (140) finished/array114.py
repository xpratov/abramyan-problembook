n = int(input("N (<= 6): "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

for i in range(2, n + 1):
    a[0] = a[i]
    j = i - 1
    
    while a[j] > a[0]:
        a[j + 1] = a[j]
        j -= 1
    
    a[j + 1] = a[0]
    
    print(f"{i-1}-bosqich:", *a[1:])