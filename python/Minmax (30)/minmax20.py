n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mn = min(numbers)
mx = max(numbers)

print(numbers.count(mn) + numbers.count(mx))
