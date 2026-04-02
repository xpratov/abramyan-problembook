a, b, c = map(float, input("3 ta haqiqiy son kiriting: ").split())

print("O'rtachasi: ")
if a>b and a<c or a<b and a>c:
  print(a)
elif b>a and b<c or b<a and b>c:
  print(b)
else:
  print(c)
    



  