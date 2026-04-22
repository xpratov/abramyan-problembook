n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

numbers.insert(k-1, 0.0)

print(numbers)