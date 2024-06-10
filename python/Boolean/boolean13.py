a, b, c = map(int, input("3ta son kiriting: ").split())

print(f"{a, b, c} sonlarining hech bo'lmaganda bittasi musbat?")
if a>0 or b>0 or c>0:
  print(True) 
else:
  print(False)