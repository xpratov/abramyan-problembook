n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

result = []
if n > 0:
    i = 0
    while i < n:
        current_val = a[i]
        start = i
        
        while i < n and a[i] == current_val:
            i += 1
        
        length = i - start
        
        for _ in range(length - 1):
            result.append(current_val)

print(result)