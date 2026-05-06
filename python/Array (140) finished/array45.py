n = int(input("N elementlar sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

min_dist = abs(a[0] - a[1])
index1, index2 = 1, 2

for i in range(n):
    for j in range(i + 1, n):
        current_dist = abs(a[i] - a[j])
        
        if current_dist < min_dist:
            min_dist = current_dist
            index1, index2 = i + 1, j + 1

print(f"Eng yaqin elementlar tartib raqamlari: {index1} {index2}")