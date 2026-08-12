s = input("Asosiy fayl nomini kiriting: ")
even_file = input("Juft sonlar fayli nomini kiriting: ")
odd_file = input("Toq sonlar fayli nomini kiriting: ")

with open(s, "r") as f:
    numbers = list(map(int, f.read().split()))

with open(even_file, "w") as f:
    for num in numbers:
        if num % 2 == 0:
            f.write(str(num) + " ")

with open(odd_file, "w") as f:
    for num in numbers:
        if num % 2 != 0:
            f.write(str(num) + " ")