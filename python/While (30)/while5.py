n = int(input("N sonini kiriting (2 ning darajasi bo'lgan son): "))

k = 0
while n > 1:
    n = n // 2 
    k += 1     

print(f"Daraja ko'rsatkichi k = {k}")