
def SortDec3(x):
  if x[0]<x[1]:
    x[0], x[1] = x[1], x[0]
  if x[1]<x[2]:
    x[1], x[2] = x[2], x[1]
  if x[0]<x[1]:
    x[0], x[1] = x[1], x[0]

array = [8, 7, 9]
SortDec3(array)

print(array)