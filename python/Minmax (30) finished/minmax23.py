n = int(input("N (N > 2): "))
numbers = list(map(float, input(f"{n} ta son kiriting: ").split()))

numbers.sort(reverse=True)

print(numbers[0], numbers[1], numbers[2])