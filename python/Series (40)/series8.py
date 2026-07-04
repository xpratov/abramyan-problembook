N = int(input())

k = 0

for _ in range(N):
  number = int(input())
  if number%2==0:
    print(number)
    k+=1
  
print(k)