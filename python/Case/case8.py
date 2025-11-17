d, m = map(int, input("D va M - kun va oy sonlarini kiriting: ").split())

if d==1:
  match m:
    case 1:
      print(31, 12)
    case 2:
      print(31, 1)
    case 3:
      print(28, 2)
    case 4:
      print(31, 3)
    case 5:
      print(30, 4)
    case 6:
      print(31, 5)
    case 7:
      print(30, 6)
    case 8:
      print(31, 7)
    case 9:
      print(31, 8)
    case 10:
      print(30, 9)
    case 11:
      print(31, 10)
    case 12:
      print(30, 11)
    case _:
      print("Sana noto'g'ri kiritilgan!")
elif d>1 and d<31 and m>1 and m<13:
  print(d-1, m)
else:
  print("Sana noto'g'ri kiritilgan!")