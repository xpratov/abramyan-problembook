p = float(input("P - haqiqiy sonini kiriting: "))

investition = 1000
k=0

while investition<1100:
  investition += investition*p/100
  k += 1

print(k, investition)