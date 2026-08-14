def SortIndex(A, N, I):
    for i in range(N):
        I.append(i)

    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[I[i]] > A[I[j]]:
                I[i], I[j] = I[j], I[i]