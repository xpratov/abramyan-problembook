a, b, c = map(float, input("3 ta haqiqiy son kiriting: ").split())

if a<b and a<c:
  print(b+c)
elif b<a and b<c:
  print(a+c)
else:
  print(a+b)