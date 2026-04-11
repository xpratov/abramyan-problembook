def RootCount(a, b, c):
  D = b**2-4*a*c
  if D==0:
    return 1
  elif D>0:
    return 2
  else:
    return 0