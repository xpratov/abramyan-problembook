n = int(input("Yil oylarining tartib raqamini kiriting: "))

result=""

match n:
  case 1:
    result="January"
  case 2:
    result="February"
  case 3:
    result="March"
  case 4:
    result="April"
  case 5:
    result="Mai"
  case 6:
    result="June"
  case 7:
    result="July"
  case 8:
    result="August"
  case 9:
    result="September"
  case 10:
    result="October"
  case 11:
    result="November"
  case 12:
    result="December"
  case _:
    result="1 dan 12 gacha son kiriting!"

print(result)