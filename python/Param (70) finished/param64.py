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


A = TPoint(0, 0)
B = TPoint(3, 4)
C = TPoint(6, 8)
D = TPoint(3, 0)

print("AB =", Leng(A, B))
print("AC =", Leng(A, C))
print("AD =", Leng(A, D))