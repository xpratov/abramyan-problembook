s = input("Matn kiriting: ")
k = int(input("K ni kiriting (0 < K < 10): "))

result = ""

for i in s:
    if i.isalpha():
        start = ord('A') if i.isupper() else ord('a')
        new_char = chr((ord(i) - start + k) % 26 + start)
        result += new_char
    else:
        result += i

print(result)