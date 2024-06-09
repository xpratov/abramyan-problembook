a, b, c = map(int, input("A, B, C sonlarini kiriting: ").split())

print("B soni A va C sonlari orasida yotadi?")
if b>a and b<c:
  print(True)
else:
  print(False)