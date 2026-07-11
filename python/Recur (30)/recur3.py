x = float(input("X - sonini kiriting: "))
n5 = list(map(int, input("N - butun son kiriting: ").split()))

def PowerN(x, n):
  if n==0:
    return 1
  elif n<0:
    return 1/PowerN(x, -n)
  else:
    if n%2==0:
      return PowerN(x, n//2)**2
    else:
      return x*(PowerN(x, n-1))

for i in n5:
  print(PowerN(x, i))
