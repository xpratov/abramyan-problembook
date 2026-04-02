a, b = map(int, input("A va B sonlarini kiriting: ").split())

print("A va B sonlarining har biri toq?")
if a%2==1 and b%2==1:
  print(True)
else:
  print(False)