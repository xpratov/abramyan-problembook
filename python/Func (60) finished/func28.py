 
def InvDigits(k):
  return int(str(k)[::-1])

numbers = [23, 45, 6754, 21345, 654]

for i in numbers: 
  print(InvDigits(i))