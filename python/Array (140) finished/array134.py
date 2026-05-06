n = int(input("N ta nuqtalar sonini kiriting (N > 1): "))
a_x = []
a_y = []

for i in range(n):
    px, py = map(float, input(f"{i}-nuqta (x y): ").split())
    a_x.append(px)
    a_y.append(py)

max_dist_sq = -1.0
p1_idx = 0
p2_idx = 0

for i in range(n):
    for j in range(i + 1, n):
        d_sq = (a_x[i] - a_x[j])**2 + (a_y[i] - a_y[j])**2
        
        if d_sq > max_dist_sq:
            max_dist_sq = d_sq
            p1_idx = i
            p2_idx = j

distance = max_dist_sq**0.5
print(f"1-nuqta (indeks {p1_idx}): ({a_x[p1_idx]}, {a_y[p1_idx]})")
print(f"2-nuqta (indeks {p2_idx}): ({a_x[p2_idx]}, {a_y[p2_idx]})")
print(f"Maximal masofa: {distance}")