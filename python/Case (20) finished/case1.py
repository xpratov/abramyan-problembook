n = int(input("Hafta kunining tartib raqamini kiriting (0<N<7): "))
result=""

match n:
  case 1:
    result="Monday"
  case 2:
    result="Tuesday"
  case 3:
    result="Wednesday"
  case 4:
    result="Thursday"
  case 5:
    result="Friday"
  case 6:
    result="Saturday"
  case 7:
    result="Sunday"

print(result)