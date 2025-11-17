arrn = list(map(int, input("Butun sonlar kiriting: ").split()))

odds=[]
evens=[]

for i in range(len(arrn)):
  if arrn[i]%2==0:
    evens.append(arrn[i])
  else:
    odds.append(arrn[i])

odds.reverse()
print(evens)
print(odds)