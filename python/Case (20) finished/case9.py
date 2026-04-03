d, m = map(int, input("D va M - kun va oy sonlarini kiriting: ").split())

match m:
  case 1:
    print((d+1, m) if d!=31 else (1, m+1))
  case 2:
    print((d+1, m) if d!=28 else (1, m+1))
  case 3:
    print((d+1, m) if d!=31 else (1, m+1))
  case 4:
    print((d+1, m) if d!=30 else (1, m+1))
  case 5:
    print((d+1, m) if d!=31 else (1, m+1))
  case 6:
    print((d+1, m) if d!=30 else (1, m+1))
  case 7:
    print((d+1, m) if d!=31 else (1, m+1))
  case 8:
    print((d+1, m) if d!=31 else (1, m+1))
  case 9:
    print((d+1, m) if d!=30 else (1, m+1))
  case 10:
    print((d+1, m) if d!=31 else (1, m+1))
  case 11:
    print((d+1, m) if d!=30 else (1, m+1))
  case 12:
    print((d+1, m) if d!=31 else (1, m+1))
  case _:
    print("Oy noto'g'ri kiritilgan!")