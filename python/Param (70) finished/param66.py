import math


class TPoint:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def Leng(A, B):
    return math.sqrt(
        (A.X - B.X) ** 2 +
        (A.Y - B.Y) ** 2
    )


class TTriangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


def Perim(T):
    return Leng(T.A, T.B) + Leng(T.A, T.C) + Leng(T.B, T.C)


def Area(T):
    AB = Leng(T.A, T.B)
    AC = Leng(T.A, T.C)
    BC = Leng(T.B, T.C)

    p = Perim(T) / 2

    return math.sqrt(
        p * (p - AB) * (p - AC) * (p - BC)
    )


A = TPoint(0, 0)
B = TPoint(3, 0)
C = TPoint(0, 4)
D = TPoint(3, 4)

ABC = TTriangle(A, B, C)
ABD = TTriangle(A, B, D)
ACD = TTriangle(A, C, D)

print("ABC:", Area(ABC))
print("ABD:", Area(ABD))
print("ACD:", Area(ACD))