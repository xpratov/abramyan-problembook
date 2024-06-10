a, b, c = map(int, input("3ta son kiriting: ").split())

print(f"{a, b, c} sonlarining faqat ikkitasi musbat?")
if a>0 and b>0 and c<0 or a<0 and b>0 and c>0 or a>0 and b<0 and c>0:
  print(True) 
else:
  print(False)