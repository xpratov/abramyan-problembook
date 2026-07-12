N = int(input())

k = 0

for i in range(N):
  number = int(input())
  if number%2!=0:
    print(number+1)
    k+=1
print(k)