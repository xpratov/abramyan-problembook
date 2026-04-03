n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

count = 0
longest = 0

for i in numbers:
    if i % 2 == 0:
        count += 1
        if count > longest:
            longest = count 
    else:
        count = 0

print(longest)