import math

def Leng(xA, yA, xB, yB):
    return math.sqrt((xA - xB)**2 + (yA - yB)**2)

print("A nuqta koordinatalari:")
xa, ya = float(input("xA = ")), float(input("yA = "))

print("B nuqta koordinatalari:")
xb, yb = float(input("xB = ")), float(input("yB = "))

print("C nuqta koordinatalari:")
xc, yc = float(input("xC = ")), float(input("yC = "))

print("D nuqta koordinatalari:")
xd, yd = float(input("xD = ")), float(input("yD = "))

print(f"\nAB uzunligi: {Leng(xa, ya, xb, yb)}")
print(f"AC uzunligi: {Leng(xa, ya, xc, yc)}")
print(f"AD uzunligi: {Leng(xa, ya, xd, yd)}")