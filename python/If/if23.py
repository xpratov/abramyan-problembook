x1, y1, x2, y2, x3, y3 = map(int, input("x1, y1, x2, y2, x3, y3 - koordinatalar tekisligida joylashgan to'g'ri to'rtburchak uchlari koordinatalarini kiriting: ").split())

x4=0
y4=0

if x2==x3:
  x4=x1
elif x1==x3:
  x4=x2
elif x1==x2:
  x4=x3

if y2==y3:
  y4=y1
elif y1==y3:
  y4=y2
elif y1==y2:
  y4=y3

print(f"To'g'ri to'rtburchakning 4-uchi koordinatasi: ({x4}; {y4}) ")