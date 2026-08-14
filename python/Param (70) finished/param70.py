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
    return (
        Leng(T.A, T.B) +
        Leng(T.A, T.C) +
        Leng(T.B, T.C)
    )


def Area(T):
    AB = Leng(T.A, T.B)
    AC = Leng(T.A, T.C)
    BC = Leng(T.B, T.C)

    p = Perim(T) / 2

    return math.sqrt(
        p * (p - AB) *
        (p - AC) *
        (p - BC)
    )


def AreaN(P, N):
    result = 0

    for i in range(1, N - 1):
        T = TTriangle(P[0], P[i], P[i + 1])
        result += Area(T)

    return result


P1 = [
    TPoint(0, 0),
    TPoint(4, 0),
    TPoint(4, 3),
    TPoint(0, 3)
]

P2 = [
    TPoint(0, 0),
    TPoint(4, 0),
    TPoint(4, 4),
    TPoint(0, 4)
]

P3 = [
    TPoint(0, 0),
    TPoint(3, 0),
    TPoint(4, 2),
    TPoint(2, 4),
    TPoint(0, 2)
]

print("P1:", AreaN(P1, 4))
print("P2:", AreaN(P2, 4))
print("P3:", AreaN(P3, 5))