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


def PerimN(P, N):
    result = 0

    for i in range(N):
        result += Leng(P[i], P[(i + 1) % N])

    return result


P1 = [
    TPoint(0, 0),
    TPoint(3, 0),
    TPoint(3, 4),
    TPoint(0, 4)
]

P2 = [
    TPoint(0, 0),
    TPoint(4, 0),
    TPoint(4, 3)
]

P3 = [
    TPoint(0, 0),
    TPoint(2, 0),
    TPoint(3, 2),
    TPoint(1, 4),
    TPoint(-1, 2)
]

print(PerimN(P1, 4))
print(PerimN(P2, 3))
print(PerimN(P3, 5))