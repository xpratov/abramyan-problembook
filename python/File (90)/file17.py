s = input("Asosiy fayl nomini kiriting: ")
s2 = input("Yangi fayl nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(int, f.read().split()))

with open(s2, "w") as f:
    if len(numbers) > 0:
        count = 1

        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1]:
                count += 1
            else:
                f.write(str(count) + " ")
                count = 1

        f.write(str(count))