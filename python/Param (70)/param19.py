def Norm1(A, M, N):
    maxi = 0

    for j in range(N):
        s = 0
        for i in range(M):
            s += abs(A[i][j])

        if s > maxi:
            maxi = s

    return maxi

