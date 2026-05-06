n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda p: (p[0] + p[1], p[0]), reverse=True)

for p in points:
    print(p[0], p[1])