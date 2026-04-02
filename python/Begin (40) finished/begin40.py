a1, b1, c1, a2, b2, c2 = map(int, input("A1, B1, C1, A2, B2, C2 - chiziqli tenglama koeffitsiyentlarini kiriting: ").split())

d = a1 * b2 - a2 * b1 

x = (c1*b2 - c2*b1) / d 
y = (a1*c2 - a2*c1) / d

print("x = ", x)
print("y = ", y)