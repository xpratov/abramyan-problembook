x1, y1, x2, y2 = map(int, input("x1, y1, x2, y2 - shaxmat doskasidagi ikkita katak koordinatasini kiriting: ").split())

if abs(x1-x2)==2 and abs(y1-y2)==1 or abs(x1-x2)==1 and abs(y1-y2)==2:
  print("Ot bir katakdan ikkinchisiga yura oladi.")
else:
  print("Ot bir katakdan ikkinchisiga yura olmaydi!")
  