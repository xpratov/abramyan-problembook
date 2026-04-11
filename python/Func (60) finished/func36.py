
def ShiftLeft3(x):
  x[0], x[1], x[2] = x[1], x[2], x[0]

array = [1, 2, 3]

ShiftLeft3(array)

print(array)