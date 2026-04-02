
def Mean(x, y):
  arif = (x+y)/2
  geom = (x*y)**(1/2)
  return arif, geom

A, B, C, D = 2.0, 8.0, 18.0, 32.0
pairs = [(A, B), (A, C), (A, D)]

for i in pairs:
  print(Mean(i[0], i[1]))
