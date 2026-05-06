n1 = int(input("A to'plamidagi nuqtalar soni: "))
a_x, a_y = [], []
print("A to'plami nuqtalarini kiriting:")
for i in range(n1):
    x, y = map(float, input(f"A[{i}]: ").split())
    a_x.append(x)
    a_y.append(y)

n2 = int(input("\nB to'plamidagi nuqtalar soni: "))
b_x, b_y = [], []
print("B to'plami nuqtalarini kiriting:")
for i in range(n2):
    x, y = map(float, input(f"B[{i}]: ").split())
    b_x.append(x)
    b_y.append(y)

min_dist_sq = float('inf')
res_a = (0, 0)
res_b = (0, 0)

for i in range(n1):
    for j in range(n2):
        d_sq = (a_x[i] - b_x[j])**2 + (a_y[i] - b_y[j])**2
        
        if d_sq < min_dist_sq:
            min_dist_sq = d_sq
            res_a = (a_x[i], a_y[i])
            res_b = (b_x[j], b_y[j])

print(f"Minimal masofa: {min_dist_sq**0.5}")
print(f"A to'plamidagi nuqta: {res_a}")
print(f"B to'plamidagi nuqta: {res_b}")