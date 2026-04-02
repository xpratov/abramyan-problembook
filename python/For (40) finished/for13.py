n = int(input("N - butun sonini kiriting: "))

result = 0

for i in range(1, n+1):
  result+=((-1)**(i+1))*(1+0.1*i)

print(round(result, 1))