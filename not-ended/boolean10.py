a, b = map(int, input("A va B sonlarini kiriting: ").split())

print("A va B sonlarining aniq bittasi toq?")
if a%2==1:
  if b%2==0:
    print(True)
if a%2==0:
  if b%2==1:
    print(False)
else:
  print(False)