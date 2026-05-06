n = int(input("N elementlar sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta saralangan son kiriting: ").split()))

if n == 0:
    count = 0
else:
    count = 1
    for i in range(1, n):
        if numbers[i] != numbers[i-1]:
            count += 1

print(f"Turli xil qiymatga ega elementlar soni: {count}")