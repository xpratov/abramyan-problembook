n = int(input())
a_x = []
a_y = []

for i in range(n):
    x, y = map(float, input().split())
    a_x.append(x)
    a_y.append(y)

def get_dist(i, j):
    return ((a_x[i] - a_x[j])**2 + (a_y[i] - a_y[j])**2)**0.5

min_p = float('inf')
vertices = (0, 0, 0)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            d1 = get_dist(i, j)
            d2 = get_dist(j, k)
            d3 = get_dist(k, i)
            
            p = d1 + d2 + d3
            
            if p < min_p:
                min_p = p
                vertices = (i, j, k)

v1, v2, v3 = vertices
print(min_p)
print(v1, v2, v3)
print(a_x[v1], a_y[v1])
print(a_x[v2], a_y[v2])
print(a_x[v3], a_y[v3])