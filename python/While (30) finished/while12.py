n = int(input("N - butun soni kiriting: "))

k = 0
summa = 0
while summa+k+1<=n:
  k+=1
  summa+=k

print(summa, k)