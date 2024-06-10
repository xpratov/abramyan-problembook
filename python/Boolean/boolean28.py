x, y = map(float, input("Ikkita haqiqiy son, nuqtaning kordinatasini kiriting: ").split())

print("Nuqta I yoki III kordinata tekisligida yotadi?")
if x>0 and y>0 or x<0 and y<0:
  print(True)
else:
  print(False)

