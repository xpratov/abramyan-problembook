a, b, c = map(int, input("A, B, C - butun sonlarni kiriting: "))

how_many = (a//c)*(b//c)
unused_area = a*b - how_many * c**2

print(how_many, unused_area)