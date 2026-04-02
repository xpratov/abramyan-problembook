n = int(input("N - detallar sonini kiriting: "))

detal_inx=0
detal_val=0

for i in range(n):
  m, v = map(float, input("m, v - detallning massasi va hajmini kiriting: ").split())
  p=m/v
  if p>detal_val:
    detal_inx=i
    detal_val=p

print(detal_inx+1, detal_val)

