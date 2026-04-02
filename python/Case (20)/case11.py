c = input("Lokatorning boshlang'ich yo'nalishini kiriting (N, W, S, E): ")
n1, n2 = map(int, input("N1, N2 - buyruqlarni kiriting: ").split())

start = 0
match c:
  case "N":
    start = 0
  case "W":
    start = 1
  case "S":
    start = 2
  case "E":
    start = 3

start= (start + n1 + n2) % 4

result = ""

match start:
  case 0:
    result = "North"
  case 1:
    result = "East"
  case 2:
    result = "South"
  case 3:
    result = "West"

print(result)



