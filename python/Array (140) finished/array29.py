n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

result = max(numbers[0::2])

print(result)