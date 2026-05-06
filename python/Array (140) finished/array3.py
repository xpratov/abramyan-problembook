n = int(input("N - butun sonlarni kiriting: "))
a, d = map(float, input("A va D - haqiqiy sonlarni kiriting: ").split())

result=[]

for i in range(n):
  result.append(a+i*d)

print(result)