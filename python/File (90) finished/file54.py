archive = input("Arxiv fayl nomi: ")
result_file = input("Natija fayli: ")

with open(archive, "r") as f:
    data = list(map(int, f.read().split()))

count = data[0]
sizes = data[1:count + 1]

index = count + 1
averages = []

for size in sizes:
    nums = data[index:index + size]

    if size > 0:
        averages.append(sum(nums) / size)
    else:
        averages.append(0)

    index += size

with open(result_file, "w") as f:
    f.write(" ".join(map(str, averages)))

print("Natija saqlandi.")