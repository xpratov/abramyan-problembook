n = int(input("N ta nuqtalar sonini kiriting: "))

a_x = []
a_y = []

print(f"{n} ta nuqta koordinatalarini kiriting:")
for i in range(n):
    px, py = map(float, input(f"{i+1}-nuqta (x y): ").split())
    a_x.append(px)
    a_y.append(py)

max_dist_sq = -1 
res_x, res_y = 0.0, 0.0

for i in range(n):
    if a_x[i] < 0 and a_y[i] > 0:
        current_dist_sq = a_x[i]**2 + a_y[i]**2
        
        if current_dist_sq > max_dist_sq:
            max_dist_sq = current_dist_sq
            res_x = a_x[i]
            res_y = a_y[i]

if max_dist_sq == -1:
    print("Ikkinchi chorakda nuqtalar mavjud emas.")
    print(f"Chiqish: ({res_x}, {res_y})")
else:
    print(f"Ikkinchi chorakdagi eng uzoq nuqta: ({res_x}, {res_y})")
    print(f"Uning masofasi: {max_dist_sq**0.5}")