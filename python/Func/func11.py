import math as m

def IsPower5(k):
  log5 = m.log(k, 5)
  return True if log5==int(log5) else False

numbers = [4, 10, 16, 25, 30, 49, 50, 64, 81, 100]
count = 0

for i in numbers:
  if IsPower5(i):
    count+=1

print(f"To'plamda {count}da 5 ning darajasi bor.")