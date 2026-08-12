archive = input("Arxiv fayli: ")
first_file = input("1-elementlar fayli: ")
last_file = input("Oxirgi elementlar fayli: ")

with open(archive, "r") as f:
    data = list(map(int, f.read().split()))

index = 0
firsts = []
lasts = []

while index < len(data):
    size = data[index]

    if size > 0:
        nums = data[index + 1:index + 1 + size]
        firsts.append(nums[0])
        lasts.append(nums[-1])

    index += size + 1

with open(first_file, "w") as f:
    f.write(" ".join(map(str, firsts)))

with open(last_file, "w") as f:
    f.write(" ".join(map(str, lasts)))

print("Natija saqlandi.")