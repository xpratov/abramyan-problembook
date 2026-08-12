s0 = input("Arxiv fayl nomi: ")
n = int(input("Fayllar soni (<=4): "))

sizes = []
all_numbers = []

for i in range(1, n + 1):
    name = input(f"S{i} fayl nomi: ")

    with open(name, "r") as f:
        nums = list(map(int, f.read().split()))

    sizes.append(len(nums))
    all_numbers.extend(nums)

with open(s0, "w") as f:
    f.write(str(n) + " ")
    f.write(" ".join(map(str, sizes)) + " ")

    if all_numbers:
        f.write(" ".join(map(str, all_numbers)))

print("Arxiv yaratildi.")