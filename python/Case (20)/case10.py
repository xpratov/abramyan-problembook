c=input("Robotning boshlang'ich yo'nalishini kiriting: ")
n=int(input("Buyruq raqamini kiriting: "))

result=""

match n:
  case 0:
    result=c
  case 1:
    match c:
      case "N":
        result="W"
      case "W":
        result="S"
      case "S":
        result="E"
      case "E":
        result="N"
      case _:
        result="Yo'nalish noto'g'ri kiritilgan!"
  case -1:
    match c:
      case "N":
        result="E"
      case "W":
        result="N"
      case "S":
        result="W"
      case "E":
        result="S"
      case _:
        result="Yo'nalish noto'g'ri kiritilgan!"
  case _:
    result="Buyruq noto'g'ri kiritilgan!"

print(result)
