n = int(input("N - to'g'ri to'rtburchaklar sonini kiriting: "))

areas=[]

for i in range(n):
  a, b = map(int, input("a, b - to'g'ri to'rtburchakning tomonlarini kiriting: ").split())
  areas.append(a*b)

print(min(areas))