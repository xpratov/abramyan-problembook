

with open("input.txt", "r") as f, \
     open("result.bin", "wb") as out:

    text = f.read()

    for char in text:
        if char in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            out.write(char.encode())