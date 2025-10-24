import math as m

x=float(input("x haqiqiy sonini kiriting: "))

result=0

if x>0:
  result = 2*m.sin(x)
else:
  result = 6-x

print("F(x) = ", result)