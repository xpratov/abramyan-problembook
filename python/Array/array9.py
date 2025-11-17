arrn = list(map(int, input("Butun sonlar kiriting: ").split()))

result=[]

for i in range(len(arrn)-1, 0, -1):
  if arrn[i]%2==0:
    result.append(arrn[i])

print(result)
print(len(result))