archive = input("Arxiv fayl nomi: ")
s = input("Natija fayli: ")
k = int(input("Qaysi faylni tiklash kerak: "))

with open(archive, "r") as f:
    data = list(map(int, f.read().split()))

count = data[0]

if k > count:
    open(s, "w").close()
    print("Bunday fayl mavjud emas.")
else:
    sizes = data[1:count + 1]

    start = count + 1

    for i in range(k - 1):
        start += sizes[i]

    end = start + sizes[k - 1]

    with open(s, "w") as f:
        f.write(" ".join(map(str, data[start:end])))

    print("Fayl tiklandi.")