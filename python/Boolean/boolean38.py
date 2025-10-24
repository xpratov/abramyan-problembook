x1, x2, y1, y2 = map(int, input("x1, x2, y1, y2 - shaxmat doskasidagi 2ta katak koordinatalarini kiriting (<8): ").split())

d1=abs(x1-x2)
d2=abs(y1-y2)

if d1==d2:
  print("Fil bir katakdan ikkinchisiga o'ta oladi.")
else:
  print("Fil bir katakdan ikkinchisiga o'ta olmaydi.")