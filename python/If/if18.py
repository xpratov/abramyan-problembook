a, b, c = map(int, input("3 ta butun son kiriting: ").split())

if b==c:
  print(1)
elif a==c:
  print(2)
elif a==b:
  print(3)
else:
  print("Sonlar bir-biriga teng emas.")