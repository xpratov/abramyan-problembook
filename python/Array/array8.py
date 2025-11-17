arrn = list(map(int, input("Butun sonlar kiriting: ").split()))

result=[]

for i in range(len(arrn)):
  if arrn[i]%2==1:
    result.append(arrn[i])

print(result)
print(len(result))