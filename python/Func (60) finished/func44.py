import math

def Atan1(x, eps):
    n = 0
    yigindi = 0
    had = x 
    
    while abs(had) >= eps:
        yigindi += had
        n += 1
        had = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        
    return yigindi

x_val = 0.5
epsilons = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

print(f"\natan({x_val}) ni hisoblash:")
for e in epsilons:
    print(f"eps={e:<10} | natija={Atan1(x_val, e):.10f}")