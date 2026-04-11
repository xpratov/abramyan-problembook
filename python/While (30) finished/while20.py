n = int(input("N - butun sonini kiriting: "))

found = False

while n > 0:
    digit = n % 10 
    if digit == 2:
        found = True
        break
    n //= 10        
print(found)