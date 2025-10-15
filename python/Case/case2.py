k=int(input("Enter examination mark: "))

result=""

match k:
  case 1:
    result="bad"
  case 2:
    result="unsatisfactory"
  case 3:
    result="mediocre"
  case 4:
    result="good"
  case 5:
    result="excellent"
  case _:
    result="error"

print(result)