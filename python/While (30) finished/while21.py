n = int(input("N - butun sonini kiriting: "))

has_odd = False

while n > 0:
    digit = n % 10 
    if digit % 2 != 0: 
        has_odd = True
        break
    n //= 10     

print(has_odd)