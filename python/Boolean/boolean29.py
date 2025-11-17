x, y, x1, y1, x2, y2 = map(float, input("x, y, x1, y1, x2, y2 - haqiqiy sonlarni kiriting: ").split())

if x<x1 and x>x2 and y>y1 and y<y2:
  print(f"{x, y} nuqta to'rtburchak ichida yotadi.")
else:
  print(f"{x, y} nuqta to'rtburchak ichida yotmaydi!")