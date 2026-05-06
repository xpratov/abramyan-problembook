n = int(input("N (<= 6): "))
a = [float(x) for x in input().split()]

for i in range(n - 1):
    last_idx = n - 1 - i
    
    max_idx = 0
    for j in range(1, last_idx + 1):
        if a[j] > a[max_idx]:
            max_idx = j
    a[max_idx], a[last_idx] = a[last_idx], a[max_idx]
    
    print(f"{i + 1}-o'tish:", *a)