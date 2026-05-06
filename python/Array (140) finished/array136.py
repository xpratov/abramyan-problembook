n = int(input("N ta nuqtalar sonini kiriting (N > 2): "))
a_x, a_y = [], []

for i in range(n):
    x, y = map(float, input(f"{i}-nuqta (x y): ").split())
    a_x.append(x)
    a_y.append(y)

min_total_dist = float('inf')
best_point = (0.0, 0.0)

for i in range(n):
    current_sum = 0.0
    for j in range(n):
        if i == j: continue 
        
        dist = ((a_x[i] - a_x[j])**2 + (a_y[i] - a_y[j])**2)**0.5
        current_sum += dist
    
    if current_sum < min_total_dist:
        min_total_dist = current_sum
        best_point = (a_x[i], a_y[i])

print(f"Tanlangan nuqta: {best_point}")
print(f"Minimal masofalar yig'indisi: {min_total_dist}")