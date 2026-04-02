a, b, c = map(float, input("Uchta haqiqiy son kiriting: ").split())

disc = b**2-4*a*c
if disc>=0:
  print("Kvadrat tenglama ildizlarga ega.")
else:
  print("Kvadrat tenglama ildizlarga ega emas!")