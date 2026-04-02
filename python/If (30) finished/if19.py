a, b, c, d = map(int, input("4 ta butun son kiriting: ").split())

if b==c==d:
  print(1)
elif a==c==d:
  print(2)
elif a==b==d:
  print(3)
elif a==b==c:
  print(4)
else:
  print("Sonlar bir-biriga teng emas.")