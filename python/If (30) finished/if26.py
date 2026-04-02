x = float(input("x sonini kiriting: "))

if x<=0:
  x=-x
elif x>0 and x<2:
  x=x**2
elif x>=2:
  x=4

print(x)