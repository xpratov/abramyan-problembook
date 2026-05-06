r_soni = float(input("R haqiqiy sonini kiriting: "))
n = int(input("N elementlar sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

min_diff = abs((a[0] + a[1]) - r_soni)
res1, res2 = a[0], a[1]

for i in range(n):
    for j in range(i + 1, n):
        current_sum = a[i] + a[j]
        current_diff = abs(current_sum - r_soni)
        
        if current_diff < min_diff:
            min_diff = current_diff
            res1 = a[i]
            res2 = a[j]

print(f"R ga eng yaqin yig'indi beruvchi elementlar: {res1} {res2}")