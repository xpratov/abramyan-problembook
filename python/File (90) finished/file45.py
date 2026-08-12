files = [
    input("1-fayl: "),
    input("2-fayl: "),
    input("3-fayl: ")
]

sizes = []

for name in files:
    with open(name, "rb") as f:
        data = f.read()
        sizes.append((len(data), name, data))

sizes.sort()

shortest = sizes[0]
longest = sizes[-1]

with open(shortest[1], "wb") as f:
    f.write(longest[2])