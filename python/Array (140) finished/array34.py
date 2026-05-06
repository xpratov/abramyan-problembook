n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

local_min_elements = []

for i in range(n):
    is_min = False
    
    if n == 1:
        is_min = True
    elif i == 0:
        if a[i] < a[i+1]:
            is_min = True
    elif i == n - 1:
        if a[i] < a[i-1]:
            is_min = True
    else:
        if a[i] < a[i-1] and a[i] < a[i+1]:
            is_min = True
            
    if is_min:
        local_min_elements.append(a[i])

if local_min_elements:
    result = max(local_min_elements)
    print("Lokal minimumlar orasida maksimali:", result)
else:
    print("Lokal minimum topilmadi.")