M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

k  = int(input("K - butun sonini kiriting: "))

for i in range(M):
  matrix[i].pop(k-1)

print(matrix)