n, k = map(float, input("N va K - haqiqiy musbat sonlarni kiriting: ").split())

quotient = 0

while n>=k:
  n = n-k
  quotient+=1

print(quotient, n)