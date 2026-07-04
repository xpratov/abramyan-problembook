N = int(input())

result = False

for i in range(N):
  number = int(input())
  if number>0:
    result = True
    break

print(result)
