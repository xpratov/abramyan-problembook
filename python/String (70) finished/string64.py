s = input("Shifrlangan matnni kiriting: ")
k = int(input("K sonini kiriting (0 < K < 10): "))

result = ""

for char in s:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        original_char = chr((ord(char) - start - k) % 26 + start)
        result += original_char
    else:
        result += char

print("Deshifrlangan matn:", result)