n = int(input("N - butun sonini kiriting: "))

result=[1]

prev=0
next=1
for i in range(n-1):
  result.append(prev+next)
  prev, next = next, prev+next

print(result)