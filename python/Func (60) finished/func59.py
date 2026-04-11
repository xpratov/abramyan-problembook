def Dist(xP, yP, xA, yA, xB, yB):
    s_pab = Area(xP, yP, xA, yA, xB, yB)
    ab = Leng(xA, yA, xB, yB)
    return 2 * s_pab / ab

xP, yP = map(float, input("P(x, y): ").split())

print(Dist(xP, yP, xA, yA, xB, yB))
print(Dist(xP, yP, xA, yA, xC, yC))
print(Dist(xP, yP, xB, yB, xC, yC))