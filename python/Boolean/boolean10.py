a, b = map(int, input("A va B sonlarini kiriting: ").split())

print("A va B sonlarining aniq bittasi toq?")
if a%2==1 and b%2==0 or b%2==1 and a%2==0:
  print(True)
else:
  print(False)