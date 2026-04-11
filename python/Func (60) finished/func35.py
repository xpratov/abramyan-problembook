
def ShiftRight3(x):
  x[0], x[1], x[2] = x[2], x[0], x[1]

array = [1, 2, 3]

ShiftRight3(array)

print(array)