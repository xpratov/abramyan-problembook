a, b, c = map(int, input("3 ta son kiriting: ").split())

manfiy=0
musbat=0

if a>0:
  musbat+=1
else: 
  manfiy+=1
if b>0:
  musbat+=1
else: 
  manfiy+=1
if c>0:
  musbat+=1
else: 
  manfiy+=1

print(f"Manfiy sonlar {manfiy} ta.")
print(f"Musbat sonlar {musbat} ta.")