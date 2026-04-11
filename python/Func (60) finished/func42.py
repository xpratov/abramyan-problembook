import math

def Cos1(x, eps):
    n = 0
    yigindi = 0
    had = 1.0 
    
    while abs(had) >= eps:
        yigindi += had
        n += 1
        had *= -1 * x**2 / ((2 * n - 1) * (2 * n))
        
    return yigindi

try:
    x_qiymati = float(input("x ni kiriting: "))
    print(f"\nx = {x_qiymati} nuqtada cos(x) ni hisoblash:\n")
    print(f"{'Epsilon (ε)':<15} | {'Cos1(x, ε)':<20} | {'math.cos(x)'}")
    print("-" * 55)
    
    eps_royxati = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    
    for eps in eps_royxati:
        natija = Cos1(x_qiymati, eps)
        haqiqiy_cos = math.cos(x_qiymati)
        print(f"{eps:<15} | {natija:<20.10f} | {haqiqiy_cos:.10f}")

except ValueError:
    print("Iltimos, faqat son kiriting!")