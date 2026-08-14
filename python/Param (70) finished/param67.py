def Dist(P, A, B):
    T = TTriangle(P, A, B)

    return 2 * Area(T) / Leng(A, B)