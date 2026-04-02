a, b, c = map(float, input("3 ta haqiqiy son kiriting: ").split())

max = 0
min = 0

if a>b and a>c:
  max = a
elif b>c and b>a:
  max = b
else:
  max = c
if a<b and a<c:
  min = a
elif b<a and b<c:
  min = b
else:
  min = c

print(min, max)
    



  