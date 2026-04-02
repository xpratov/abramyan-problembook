pi = 3.14
S = int(input("Doira yuzini kiriting: "))

def intacter2(num):
  return (int(num*100))/100

diameter = 2*(S/pi)**2
print(f"Diametri: {intacter2(diameter)}")
print(f"Uzunligi: {intacter2(pi*diameter)}")