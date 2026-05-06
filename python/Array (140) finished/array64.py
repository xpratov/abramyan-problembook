a = [100, 80, 60, 40]
b = [95, 85, 75]
c = [110, 90, 70, 50, 30]

n_a, n_b, n_c = len(a), len(b), len(c)
d = []

i, j, k = 0, 0, 0

while i < n_a or j < n_b or k < n_c:
    val_a = a[i] if i < n_a else float('-inf')
    val_b = b[j] if j < n_b else float('-inf')
    val_c = c[k] if k < n_c else float('-inf')
    
    max_val = max(val_a, val_b, val_c)
    
    if max_val == val_a and i < n_a:
        d.append(a[i])
        i += 1
    elif max_val == val_b and j < n_b:
        d.append(b[j])
        j += 1
    else:
        d.append(c[k])
        k += 1

print("Natijaviy D massivi:")
print(d)