n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

min_indices = []

for i in range(n):
    if n < 2:
        break
        
    if i == 0:
        if a[i] < a[i+1]:
            min_indices.append(i)
            
    elif i == n - 1:
        if a[i] < a[i-1]:
            min_indices.append(i)
            
    else:
        if a[i] < a[i-1] and a[i] < a[i+1]:
            min_indices.append(i)

for idx in min_indices:
    a[idx] = a[idx] ** 2

print("Natija:", a)