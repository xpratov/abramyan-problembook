archive = input("Arxiv fayli: ")
result = input("Natija fayli: ")
k = int(input("Qaysi fayl kerak: "))

with open(archive, "r") as f:
    data = list(map(int, f.read().split()))

index = 0
current = 1
found = False

while index < len(data):
    size = data[index]

    if current == k:
        nums = data[index + 1:index + 1 + size]

        with open(result, "w") as out:
            out.write(" ".join(map(str, nums)))

        found = True
        break

    index += size + 1
    current += 1

if not found:
    open(result, "w").close()
    print("Bunday fayl mavjud emas.")
else:
    print("Fayl tiklandi.")