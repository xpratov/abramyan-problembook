x = float(input("x - haqiqiy sonni kiriting: "))

if x<0:
  x=0
elif int(x)%2==0:
  x=1
elif int(x)%2==1:
  x=-1

print("F(x) = ", x)
