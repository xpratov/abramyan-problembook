b, c = map(float, input("B va C - haqiqiy sonlarni kiriting: ").split())
numbers = list(map(float, input("10 ta haqiqiy son kiriting: ").split()))

inners = [i for i in numbers if i>b and i<c] 

if not inners:
  print(0.0, 0)
else:
  mx = max(inners)
  count = 1
  for i in numbers:
    if i==mx:
      print(mx, count)
      break
    count+=1
  