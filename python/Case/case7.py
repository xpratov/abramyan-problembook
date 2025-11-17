n = int(input("N sonini kiriting: "))
m = float(input("M sonini kiriting: "))

result=" kilogram"

match n:
  case 1:
    result=str(m) + result
  case 2:
    result=str(m/10000) + result
  case 3:
    result=str(m/1000)+result
  case 4:
    result=str(m*1000) + result
  case 5:
    result=str(m*100) + result
  case _:
    result="N soni 1 dan 5 gacha bo'lishi kerak."
  
print(result)