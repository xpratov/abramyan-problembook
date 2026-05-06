n = int(input("N ni kiriting: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

seen = set()
first_error_index = 0

for i in range(n):
    if a[i] < 1 or a[i] > n or a[i] in seen:
        first_error_index = i + 1  
        break
    
    seen.add(a[i])

print(first_error_index)