n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

local_max_elements = []

for i in range(n):
    is_max = False
    
    if n == 1:
        is_max = True
    elif i == 0:
        if a[i] > a[i+1]:
            is_max = True
    elif i == n - 1:
        if a[i] > a[i-1]:
            is_max = True
    else:
        if a[i] > a[i-1] and a[i] > a[i+1]:
            is_max = True
            
    if is_max:
        local_max_elements.append(a[i])

if local_max_elements:
    result = min(local_max_elements)
    print("Lokal maksimumlar orasida minimali:", result)
else:
    print("Lokal maksimum topilmadi.")