K = int(input("K = "))
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

paragraphs = []
start = None

for i, line in enumerate(lines):
    if line.strip() != "":
        if start is None:
            start = i
    else:
        if start is not None:
            paragraphs.append((start, i))
            start = None

if start is not None:
    paragraphs.append((start, len(lines)))

if 1 <= K <= len(paragraphs):
    start, end = paragraphs[K - 1]

    del lines[start:end]

    with open(filename, "w") as f:
        f.writelines(lines)