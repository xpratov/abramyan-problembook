n = int(input("N - butun sonini kiriting: "))

res = 0

while n > 0:
    digit = n % 10      
    res = res * 10 + digit 
    n //= 10            

print(res)