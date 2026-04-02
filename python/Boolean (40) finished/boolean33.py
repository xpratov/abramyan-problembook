a, b, c = map(int, input("Uchburchakning 3ta tomonlarini kiriting: ").split())

print("Uchburchak bo'la oladimi?")
if a+b>c or b+c>a or a+c>b:
  print(True)
else:
  print(False)