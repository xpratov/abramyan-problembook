def SortCols(A, M, N):
    cols = []

    for j in range(N):
        col = []
        for i in range(M):
            col.append(A[i][j])
        cols.append(col)

    cols.sort()

    for j in range(N):
        for i in range(M):
            A[i][j] = cols[j][i]


M = int(input())
N = int(input())

A = []
for i in range(M):
    A.append(list(map(int, input().split())))

SortCols(A, M, N)

for row in A:
    print(*row)