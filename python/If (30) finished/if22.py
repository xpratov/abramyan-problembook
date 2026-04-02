x, y = map(int, input("x, y - koordinata tekisligida joylashgan nuqta koordinatalarini kiriting: ").split())

if x>0 and y>0:
  print("1-chorakda joylashgan.")
elif x<0 and y>0:
  print("2-chorakda joylashgan.")
elif x<0 and y<0:
  print("3-chorakda joylashgan.")
elif x>0 and y<0:
  print("4-chorakda joylashgan.")
