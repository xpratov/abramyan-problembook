n = int(input("N ta nuqtalar sonini kiriting: "))

a_x = [] 
a_y = [] 

print(f"{n} ta nuqta koordinatalarini kiriting:")
for i in range(n):
    px, py = map(float, input(f"{i+1}-nuqta (x y): ").split())
    a_x.append(px)
    a_y.append(py)

bx, by = map(float, input("B nuqtasi koordinatalarini kiriting (x y): ").split())

min_dist_sq = (a_x[0] - bx)**2 + (a_y[0] - by)**2
nearest_index = 0

for i in range(1, n):
    current_dist_sq = (a_x[i] - bx)**2 + (a_y[i] - by)**2
    
    if current_dist_sq < min_dist_sq:
        min_dist_sq = current_dist_sq
        nearest_index = i

print(f"B nuqtasiga eng yaqin nuqta: ({a_x[nearest_index]}, {a_y[nearest_index]})")
print(f"Masofaning kvadrati: {min_dist_sq}")
print(f"Haqiqiy masofa: {min_dist_sq**0.5}")