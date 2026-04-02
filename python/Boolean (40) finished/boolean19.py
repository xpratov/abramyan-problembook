a, b, c = map(int, input("a, b, c butun sonlarni kiriting: ").split())

if a!=b and abs(a)==abs(b) or b!=c and abs(b)==abs(c) or a!=c and abs(a)==abs(c):
  print("Berilgan sonlardan kamida 2 tasi bir biriga qarama-qarshi (a, -a).")
else:
  print("Berilgan sonlardan kamida 2 tasi bir biriga qarama-qarshi (a, -a) emas. ")