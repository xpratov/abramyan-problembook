n = int(input("n - 1 dan 999 gacha bo'lgan butun son kiriting: "))

result=""

digits=len(str(n))

if digits==1:
  result="one-digit"
elif digits==2:
  result="two-digit"
elif digits==3:
  result="three-digit"

if n%2==0:
  result+=" even"
else:
  result+=" odd"

print(result+" number")

