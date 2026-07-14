M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

local_mins = []

directions = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),           (0, 1), 
              (1, -1),  (1, 0),  (1, 1)]

for i in range(M):
    for j in range(N):
        is_local_min = True
        current_val = matrix[i][j]
        
        has_neighbor = False 
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < M and 0 <= nj < N:
                has_neighbor = True
                if current_val >= matrix[ni][nj]:
                    is_local_min = False
                    break
        
        if is_local_min and has_neighbor:
            local_mins.append((i, j))

for r, c in local_mins:
    matrix[r][c] = 0

print(matrix)