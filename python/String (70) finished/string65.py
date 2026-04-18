s = input("Shifrlangan matnni kiriting: ")
c_asl = input("Asl holatdagi birinchi harfni kiriting: ")

c_shifr = s[0]

start_shifr = ord('A') if c_shifr.isupper() else ord('a')
start_asl = ord('A') if c_asl.isupper() else ord('a')

pos_shifr = ord(c_shifr) - start_shifr
pos_asl = ord(c_asl) - start_asl

k = (pos_shifr - pos_asl) % 26

print(f"Topilgan K qadami: {k}")
result = ""
for char in s:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        original_char = chr((ord(char) - start - k) % 26 + start)
        result += original_char
    else:
        result += char

print("Deshifrlangan matn:", result)