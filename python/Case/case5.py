n, a, b = map(int, input("n, a, b - sonlarni kiriting: ").split())

result=0

match n:
  case 1:
    result=a+b
  case 2:
    result=a-b
  case 3:
    result=a*b
  case 4:
    result=a/b
  case _:
    result="n soni 1 dan 4 gacha bo'lishi kerak."
  
print(result)