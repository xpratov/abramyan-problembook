with open("input.txt", "r") as f, \
     open("result.bin", "wb") as out:

    text = f.read()
    seen = set()

    for char in text:
        if char not in seen:
            seen.add(char)
            out.write(char.encode())