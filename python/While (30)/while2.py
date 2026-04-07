a, b = map(float, input("A va B - haqiqiy musbat sonlarni kiriting: ").split())

count = 0
while a>=b:
  a = a-b
  count+=1

print(count)