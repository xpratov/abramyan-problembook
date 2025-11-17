n = int(input("N sonini kiriting: "))
l = float(input("L sonini kiriting: "))

result=" meter"

match n:
  case 1:
    result=str(l/10) + result
  case 2:
    result=str(l*1000) + result
  case 3:
    result=str(l)+result
  case 4:
    result=str(l/1000) + result
  case 5:
    result=str(l/100) + result
  case _:
    result="N soni 1 dan 5 gacha bo'lishi kerak."
  
print(result)