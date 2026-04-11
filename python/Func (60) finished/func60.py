def Alts(xA, yA, xB, yB, xC, yC):
    hA = Dist(xA, yA, xB, yB, xC, yC)
    hB = Dist(xB, yB, xA, yA, xC, yC)
    hC = Dist(xC, yC, xA, yA, xB, yB)
    return hA, hB, hC

print(Alts(xA, yA, xB, yB, xC, yC))
print(Alts(xA, yA, xB, yB, xD, yD))
print(Alts(xA, yA, xC, yC, xD, yD))