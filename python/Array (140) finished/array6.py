n, a, b = map(int, input("N, A, B - butun sonlarni kiriting: ").split())

result=[]

for i in range(n):
  if i==0:
    result.append(a)
  elif i==1:
    result.append(b)
  else:
    result.append(sum(result))

print(result)