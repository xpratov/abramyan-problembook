def DecodeText(S, K):
    with open(S, "r", encoding="utf-8") as f:
        text = f.read()

    result = ""

    for ch in text:

        if 'A' <= ch <= 'Z':
            ch = chr((ord(ch) - ord('A') - K) % 26 + ord('A'))

        elif 'a' <= ch <= 'z':
            ch = chr((ord(ch) - ord('a') - K) % 26 + ord('a'))

        result += ch

    with open(S, "w", encoding="utf-8") as f:
        f.write(result)


S = input()
K = int(input())

DecodeText(S, K)