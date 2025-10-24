n = int(input("Yil oylarining tartib raqamini kiriting: "))

result=""

match n:
  case 1 | 2 | 12:
    result="Winter"
  case 3 | 4 | 5:
    result="Spring"
  case 6 | 7 | 8:
    result="Summer"
  case 9 | 10 | 11:
    result="Autumn"
  case _:
    result="1 dan 12 gacha son kiriting!"

print(result)