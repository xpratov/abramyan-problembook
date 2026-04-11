import math

def Leng(xA, yA, xB, yB):
    return math.sqrt((xA - xB)**2 + (yA - yB)**2)

def Perim(xA, yA, xB, yB, xC, yC):
    ab = Leng(xA, yA, xB, yB)
    bc = Leng(xB, yB, xC, yC)
    ac = Leng(xA, yA, xC, yC)
    return ab + bc + ac

xA, yA = map(float, input("A(x, y): ").split())
xB, yB = map(float, input("B(x, y): ").split())
xC, yC = map(float, input("C(x, y): ").split())
xD, yD = map(float, input("D(x, y): ").split())

print(Perim(xA, yA, xB, yB, xC, yC))
print(Perim(xA, yA, xB, yB, xD, yD))
print(Perim(xA, yA, xC, yC, xD, yD))