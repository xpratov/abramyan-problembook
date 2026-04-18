s = input("Satr kiriting: ")
n = int(input("Butun son kiriting: "))

if len(s)>n:
  print(s[-n:])
elif len(s)<n:
  print("."*(n-len(s))+s)
else: 
  print(s)