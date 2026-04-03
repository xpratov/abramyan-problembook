n = int(input("N - to'g'ri to'rtburchaklar sonini kiriting: "))

perimeters=[]

for i in range(n):
  a, b = map(int, input("a, b - to'g'ri to'rtburchakning tomonlarini kiriting: ").split())
  perimeters.append(2*(a+b))

print(max(perimeters))