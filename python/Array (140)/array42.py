r_soni = float(input("R haqiqiy sonini kiriting: "))
n = int(input("N elementlar sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta sonni kiriting: ").split()))

min_diff = abs((numbers[0] + numbers[1]) - r_soni)
res1, res2 = numbers[0], numbers[1]

for i in range(len(numbers) - 1):
    current_sum = numbers[i] + numbers[i+1]
    current_diff = abs(current_sum - r_soni)
    
    if current_diff < min_diff:
        min_diff = current_diff
        res1 = numbers[i]
        res2 = numbers[i+1]

print(f"R ga eng yaqin yig'indi beruvchi juftlik: {res1} {res2}")