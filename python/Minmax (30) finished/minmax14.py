b = float(input("B - musbat haqiqiy son kiriting: "))
numbers = list(map(float, input("10 ta haqiqiy son kiriting: ").split()))

biggers = [i for i in numbers if i>b]

if not biggers:
  print(0.0, 0)  
else: 
  mn = min(biggers)
  count = 1
  for i in numbers: 
    if i==mn:
      print(mn, count)
      break
    count +=1

