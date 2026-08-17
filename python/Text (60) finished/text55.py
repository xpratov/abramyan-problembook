with open("input.txt", "r") as f, \
     open("result.bin", "wb") as out:

    text = f.read()

    chars = set(text)

    for char in sorted(chars):
        out.write(char.encode())