s = input("Matn kiriting: ")

result = ""

for i in s:
  result+=chr(ord(i)+1)

print(result)