def TriangleP(a, h):
  b2=(a/2)**2+h**2
  b=b2**(1/2)
  return a+b*2

a, h = map(float, input("a, h - Uchburchakning asosi va balandligini kiriting: ").split())

print("Perimetr: ", TriangleP(a, h))