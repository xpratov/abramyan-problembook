x1, x2, y1, y2 = map(int, input("x1, x2, y1, y2 - shaxmat doskasidagi 2ta katak koordinatalarini kiriting (<8): ").split())

d1=abs(x1-x2)
d2=abs(y1-y2)

if d1<2 and d2<2:
  print("Shox bir katakdan ikkinchisiga o'ta oladi.")
else:
  print("Shox bir katakdan ikkinchisiga o'ta olmaydi.")