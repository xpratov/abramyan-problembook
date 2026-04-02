a, b, c = map(int, input("A, B, C - son o'qidagi 3 ta nuqta qiymatini kiriting: ").split())

differB=abs(a-b)
differC=abs(a-c)

if differB<differC:
  print(f"B nuqta A nuqtaga {differB} yaqinroq.")
else:
  print(f"C nuqta A nuqtaga {differC} yaqinroq.")