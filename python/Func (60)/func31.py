
def Swap(x, i, j):
  x[i], x[j] = x[j], x[i]

array = [1, 2, 3, 4]

Swap(array, 0, 1)
Swap(array, 2, 3)
Swap(array, 1, 2)

print(array)