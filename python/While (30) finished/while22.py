n = int(input("N - butun sonini kiriting: "))

prime = True
div = 2
while div<n:
  if n%div == 0:
    prime = False
    break
  div+=1
  
print(prime)
