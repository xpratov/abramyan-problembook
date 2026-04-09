import math

def Power4(x, a, eps):
    n = 0
    yigindi = 1.0  
    had = a * x    
    
    joriy_had = 1.0
    yigindi = 0
    n = 0
    
    while True:
        if n == 0:
            joriy_had = 1.0
        else:
            joriy_had *= x * (a - n + 1) / n
            
        if abs(joriy_had) < eps:
            break
            
        yigindi += joriy_had
        n += 1
        
    return yigindi

x_val = 0.5
a_val = 2.0
epsilons = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

print(f"\n(1 + {x_val})^{a_val} ni hisoblash:")
for e in epsilons:
    print(f"eps={e:<10} | natija={Power4(x_val, a_val, e):.10f}")