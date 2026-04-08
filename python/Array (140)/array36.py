n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

suitable_elements = []

for i in range(n):
    is_local_min = False
    is_local_max = False
    
    if n == 1:
        is_local_min = True
        is_local_max = True
    elif i == 0:
        if a[i] < a[i+1]: is_local_min = True
        if a[i] > a[i+1]: is_local_max = True
    elif i == n - 1:
        if a[i] < a[i-1]: is_local_min = True
        if a[i] > a[i-1]: is_local_max = True
    else:
        if a[i] < a[i-1] and a[i] < a[i+1]: is_local_min = True
        if a[i] > a[i-1] and a[i] > a[i+1]: is_local_max = True

    if not is_local_min and not is_local_max:
        suitable_elements.append(a[i])

if suitable_elements:
    print(max(suitable_elements))
else:
    print(0.0)