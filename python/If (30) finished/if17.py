a, b, c = map(float, input("3 ta haqiqiy son kiriting: ").split())

if a<b and b<c or c<b and b<a:
  a=a*2
  b=b*2
  c=c*2
else:
  a=-a
  b=-b
  c=-c

print(a, b, c)