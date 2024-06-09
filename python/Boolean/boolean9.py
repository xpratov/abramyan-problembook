a, b = map(int, input("A va B sonlarini kiriting: ").split())

print("A va B sonlarining kamida bittasi toq?")
if a%2==1 or b%2==1:
  print(True)
else:
  print(False)