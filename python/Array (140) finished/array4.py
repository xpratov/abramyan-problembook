n = int(input("N - butun sonlarni kiriting: "))
a, r = map(float, input("A va R - haqiqiy sonlarni kiriting: ").split())

result=[]

for i in range(n):
  result.append(a*r**i)

print(result)