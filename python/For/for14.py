n = int(input("N - butun sonini kiriting: "))

n2=0

for i in range(1, 2*n, 2):
  n2+=i

print(f"{n} ning kvadrati: ", n2)