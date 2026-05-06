n = int(input("N ta nuqtalar sonini kiriting: "))
a_x = []
a_y = []

print(f"{n} ta nuqta koordinatalarini kiriting:")
for i in range(n):
    px, py = map(float, input(f"{i+1}-nuqta (x y): ").split())
    a_x.append(px)
    a_y.append(py)

min_dist_sq = float('inf') 
res_x, res_y = 0.0, 0.0

for i in range(n):
    if (a_x[i] > 0 and a_y[i] > 0) or (a_x[i] < 0 and a_y[i] < 0):
        current_dist_sq = a_x[i]**2 + a_y[i]**2
        
        if current_dist_sq < min_dist_sq:
            min_dist_sq = current_dist_sq
            res_x = a_x[i]
            res_y = a_y[i]

print("\nNatija:")
if min_dist_sq == float('inf'):
    print("1- yoki 3-chorakda nuqtalar mavjud emas.")
    print(f"Chiqish: ({res_x}, {res_y})")
else:
    print(f"Eng yaqin nuqta: ({res_x}, {res_y})")
    print(f"Haqiqiy masofa: {min_dist_sq**0.5}")