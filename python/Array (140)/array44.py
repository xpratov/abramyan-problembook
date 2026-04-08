n = int(input("N elementlar sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta sonni kiriting: ").split()))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            print(f"Bir xil elementlarning tartib raqamlari: {i + 1} {j + 1}")
            found = True
            break
    if found:
        break