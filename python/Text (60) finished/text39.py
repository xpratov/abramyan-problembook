filename = input("Fayl nomi: ")
new_filename = input("Yangi fayl nomi: ")
K = int(input("K = "))

with open(filename, "r") as f:
    lines = f.readlines()

result = []
paragraph = []


def format_paragraph(paragraph):
    words = []

    for line in paragraph:
        words.extend(line.split())

    formatted = []
    current = ""

    for word in words:
        if current == "":
            current = word

        elif len(current) + 1 + len(word) <= K:
            current += " " + word

        else:
            formatted.append(current)
            current = word

    if current:
        formatted.append(current)

    return formatted


for line in lines:
    line = line.rstrip()

    if line.startswith("     "):

        if paragraph:
            result.extend(format_paragraph(paragraph))
            paragraph = []

        line = line[5:]

        paragraph.append(line)

    else:
        paragraph.append(line)

if paragraph:
    result.extend(format_paragraph(paragraph))


with open(new_filename, "w") as f:
    f.write("\n".join(result))