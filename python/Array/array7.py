arrn=list(map(float, input("Haqiqiy sonlardan iborat massiv kiriting: ").split()))

result=[]

for i in range(len(arrn), 0, -1):
  result.append(arrn[i-1])

print(result)
