
def Sin1(x, e):
    term = x   
    summa = x  
    n = 1
    
    while True:
        term *= -x**2 / ((2*n) * (2*n + 1))
        
        if abs(term) < e:
            break
            
        summa += term
        n += 1
        
    return summa

# Tekshirish
print(Sin1(1.57, 0.0001))