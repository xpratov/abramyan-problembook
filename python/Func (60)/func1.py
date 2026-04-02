a, b = map(int, input("A va B sonlarini kiriting: ").split())

def sign(x):
  if x<0:
    return -1
  elif x==0:
    return 0
  else:
    return 1

print( sign(a) + sign(b))