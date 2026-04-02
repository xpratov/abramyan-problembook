a, b, c = map(int, input("a, b, c butun sonlarni kiriting: ").split())

if a==b or b==c or a==c:
  print("Berilgan sonlardan kamida 2 tasi teng.")
else:
  print("Berilgan sonlardan kamida 2 tasi teng emas.")