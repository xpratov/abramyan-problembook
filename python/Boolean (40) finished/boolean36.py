x1, y1 = map(int, input("Shaxmat doskasidagi bitta katak kordinatasini kiriting: ").split())
x2, y2 = map(int, input("Shaxmat doskasidagi bitta katak kordinatasini kiriting: ").split())

if x1==x2 or y1==y2:
  print("Rux bir katakdan ikkinchisiga o'ta oladi.")
else:
  print("Rux bir katakdan ikkinchisiga o'ta olmaydi.")