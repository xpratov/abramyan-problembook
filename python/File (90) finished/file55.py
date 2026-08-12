s0 = input("Arxiv fayl nomi: ")
n = int(input("Fayllar soni (<=4): "))

with open(s0, "w") as out:
    for i in range(1, n + 1):
        name = input(f"S{i} fayl nomi: ")

        with open(name, "r") as f:
            nums = list(map(int, f.read().split()))

        out.write(str(len(nums)) + " ")

        if nums:
            out.write(" ".join(map(str, nums)) + " ")

print("Arxiv yaratildi.")