n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta son kiriting: ").split()))

min_positive = None

for i in numbers:
    if i > 0:
        if min_positive is None or i < min_positive:
            min_positive = i

if min_positive is None:
    print(0)
else:
    print(min_positive)