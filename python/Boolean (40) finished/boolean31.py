a, b, c = map(int, input("Uchburchakning 3ta tomonlarini kiriting: ").split())

print("Uchburchak teng yonli uchburchak?")
if a==b or b==c or a==c:
  print(True)
else:
  print(False)