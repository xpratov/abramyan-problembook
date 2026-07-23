s = input("Asosiy fayl nomini kiriting: ")
positive_file = input("Musbat sonlar fayli nomini kiriting: ")
negative_file = input("Manfiy sonlar fayli nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(int, f.read().split()))

with open(positive_file, "w") as f:
    for num in reversed(numbers):
        if num > 0:
            f.write(str(num) + " ")

with open(negative_file, "w") as f:
    for num in reversed(numbers):
        if num < 0:
            f.write(str(num) + " ")