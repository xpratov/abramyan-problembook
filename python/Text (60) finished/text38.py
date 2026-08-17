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

    lines_result = []
    current = ""

    for word in words:
        if current == "":
            current = word
        elif len(current) + 1 + len(word) <= K:
            current += " " + word
        else:
            lines_result.append(current)
            current = word

    if current:
        lines_result.append(current)

    return lines_result


for line in lines:
    line = line.rstrip("\n")

    if line == "":
        if paragraph:
            result.extend(format_paragraph(paragraph))
            paragraph = []

        result.append("")
    else:
        paragraph.append(line)

if paragraph:
    result.extend(format_paragraph(paragraph))


with open(new_filename, "w") as f:
    f.write("\n".join(result))