
def TrianglePS(a):
  p = a*3
  s = a**2 * (3**(1/2) / 4)
  return p, s

sides = [5.0, 10.0, 7.5]

for i in sides:
  print(TrianglePS(i))

