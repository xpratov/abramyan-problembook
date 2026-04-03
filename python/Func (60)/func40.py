
def Exp1(x, e):
  summma = 1.0
  term = 1.0
  n = 1

  while True: 
    term = term * x/n
    if abs(term)<e:
      break
    summma += term
    n+=1
  return summma

# Kirish ma'lumotlari
x_val = float(input("x ni kiriting: "))

eps_list = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

print(f"exp({x_val}) ning taqribiy qiymatlari:\n")
print(f"{'Epsilon':<10} | {'Natija':<20}")
print("-" * 35)

for e in eps_list:
    result = Exp1(x_val, e)
    print(f"{e:<10} | {result:<20.8f}")
