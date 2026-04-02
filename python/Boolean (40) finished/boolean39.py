x1, y1, x2, y2 = map(int, input("x1, y1, x2, y2 - shaxmat doskasidagi ikkita katak koordinatasini kiriting: ").split())

if abs(x1-x2)==abs(y1-y2) or (x1==x2 or y1==y2):
  print("Farzin bir katakdan ikkinchisiga yura oladi.")
else:
  print("Farzin bir katakdan ikkinchisiga yura olmaydi!")