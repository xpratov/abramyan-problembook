
def Minmax(x, i, j):
  if x[i]>x[j]:
    x[i], x[j] = x[j], x[i]

array = [5, 7, 2, 8]

Minmax(array, 0, 1)
Minmax(array, 1, 2)
Minmax(array, 2, 3)
Minmax(array, 0, 1)

print(array[0], array[-1])