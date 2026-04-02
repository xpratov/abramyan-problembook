def Calc(a, b, o):
  match o:
    case 1:
      return a-b
    case 2:
      return a*b
    case 3:
      return a/b
    case _:
      return a+b

a, b = map(float, input("A, B - haqiqiy sonlarni kiriting: ").split())
oper = int(input("Operatsiya indeksini kiriting: "))

print(Calc(a, b, oper))