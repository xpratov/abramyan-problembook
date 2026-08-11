def RemoveLineNumbers(S):
    with open(S, "r") as f:
        lines = f.readlines()

    result = []

    for line in lines:
        text = line.rstrip("\n")

        i = 0

        # Boshidagi bo'sh joylarni o'tkazib yuboramiz
        while i < len(text) and text[i] == " ":
            i += 1

        # Raqamlarni tekshiramiz
        start = i

        while i < len(text) and text[i].isdigit():
            i += 1

        # Agar raqam topilgan bo'lsa
        if i > start:
            # Raqamdan keyingi bo'sh joylarni olib tashlaymiz
            while i < len(text) and text[i] == " ":
                i += 1

            result.append(text[i:] + "\n")
        else:
            result.append(line)

    with open(S, "w") as f:
        f.writelines(result)


S = input()

RemoveLineNumbers(S)