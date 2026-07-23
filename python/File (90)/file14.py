s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(float, f.read().split()))

average = sum(numbers) / len(numbers)

print(average)