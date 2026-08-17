S = input("S = ")

with open("input.txt", "r") as f:
    text = f.read()

result = ""

for i, char in enumerate(text):
    if 'a' <= char <= 'z':
        shift = int(S[i % 10]) + 1

        new_char = chr(
            (ord(char) - ord('a') + shift) % 26 + ord('a')
        )

        result += new_char

    elif 'A' <= char <= 'Z':
        shift = int(S[i % 10]) + 1

        new_char = chr(
            (ord(char) - ord('A') + shift) % 26 + ord('A')
        )

        result += new_char

    else:
        result += char

with open("input.txt", "w") as f:
    f.write(result)