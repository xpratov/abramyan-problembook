with open("input.txt", "r") as f:
    text = f.read()

counts = {}

for char in text:
    if 'a' <= char <= 'z':
        counts[char] = counts.get(char, 0) + 1

items = list(counts.items())

items.sort(key=lambda item: (-item[1], item[0]))

with open("result.bin", "wb") as out:
    for letter, count in items:
        result = f"{letter}-{count}"
        out.write(result.encode() + b"\n")