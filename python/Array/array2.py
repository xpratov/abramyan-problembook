n = int(input("N - butun sonni kiriting: "))

current_item=2
result=[]

for i in range(n):
  result.append(current_item)
  current_item=current_item*2

print(result)