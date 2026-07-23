s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(float, f.read().split()))

for i in range(len(numbers) - 2, 0, -1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        print(numbers[i])
        break