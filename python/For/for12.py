n = int(input("N - butun sonini kiriting: "))
n=n*10

total=1
for i in range(11, n+1):
  total*=i/10

print(total)

