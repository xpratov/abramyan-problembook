x, y = map(int, input("x, y - koordinata tekisligida joylashga nuqta koordinatalarini kiriting: ").split())

if x==0 and y==0:
  print(0)
elif x==0:
  print(1)
elif y==0:
  print(2)
else:
  print(3)