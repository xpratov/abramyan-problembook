n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

last_local_max = -1

for i in range(n - 1, -1, -1):
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
        last_local_max = i + 1
        break

print(last_local_max)