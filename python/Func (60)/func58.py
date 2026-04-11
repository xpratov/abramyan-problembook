def Area(xA, yA, xB, yB, xC, yC):
    p = Perim(xA, yA, xB, yB, xC, yC) / 2
    ab = Leng(xA, yA, xB, yB)
    bc = Leng(xB, yB, xC, yC)
    ac = Leng(xA, yA, xC, yC)
    return math.sqrt(p * (p - ab) * (p - bc) * (p - ac))

print(Area(xA, yA, xB, yB, xC, yC))
print(Area(xA, yA, xB, yB, xD, yD))
print(Area(xA, yA, xC, yC, xD, yD))