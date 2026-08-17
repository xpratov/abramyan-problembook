filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

result = []
paragraph = []

def format_line(line):
    words = line.split()

    if len(words) == 1:
        return words[0]

    spaces = len(words) - 1
    text_length = sum(len(word) for word in words)

    extra = 50 - text_length
    base = extra // spaces
    remainder = extra % spaces

    gaps = [base] * spaces

    for i in range(spaces - 1, spaces - remainder - 1, -1):
        gaps[i] += 1

    result_line = words[0]

    for i in range(spaces):
        result_line += " " * gaps[i]
        result_line += words[i + 1]

    return result_line


for line in lines:
    line = line.rstrip("\n")

    if line == "":
        if paragraph:
            for i in range(len(paragraph) - 1):
                result.append(format_line(paragraph[i]))

            result.append(paragraph[-1])

            paragraph = []

        result.append("")
    else:
        paragraph.append(line)

if paragraph:
    for i in range(len(paragraph) - 1):
        result.append(format_line(paragraph[i]))

    result.append(paragraph[-1])


with open(filename, "w") as f:
    f.write("\n".join(result))