a, b, c = map(int, input("A, B, C - kvadrat tenglamaning koeffitsiyentlarini kiriting: ").split())

d = b**2 - 4*a*c 

x1 = (-b+d**(1/2))/(2*a)
x2 = (-b-d**(1/2))/(2*a)

print(f"Kvadrat tenglamaning ildizlari:\nX1 = {x1}\nX2 = {x2}")
