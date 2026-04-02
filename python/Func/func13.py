
def IsPrime(n):
  for i in range(2, n):
    if n%i==0:
      return False
  return True

numbers = [4, 10, 16, 25, 30, 49, 50, 64, 81, 100]
count = 0

for i in numbers:
  if IsPrime(i):
    count+=1

print(f"To'plamda {count} ta TUB son bor.")