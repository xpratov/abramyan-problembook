def Quarter(x, y):
  if x>0:
    if y>0:
      return 1
    elif y<0:
      return 4
  elif x<0:
    if y>0:
      return 2
    elif y<0:
      return 3
  return "chiziqda"

print(Quarter(3, -5))
print(Quarter(-6, -2))
print(Quarter(-2, 4))