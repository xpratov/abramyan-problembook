s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(int, f.read().split()))

count = 0

if len(numbers) > 0:
    count = 1

    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            count += 1

print(count)