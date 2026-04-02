
def Fib(n):
  if n<=2:
    return 1
  prev = 1
  nex = 1
  for i in range(3, n+1):
    prev, nex = nex, nex+prev
  return nex

numbers = [23, 56, 879, 12, 5]

for i in numbers:
  print(Fib(i))



