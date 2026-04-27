M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting (haqiqiy sonlar):")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

elements = sum(matrix, [])

minel = min(elements)
maxel = max(elements)

minel_inx = 0
maxel_inx = 0

for i in range(M):
  if minel in matrix[i]:
    minel_inx = i
  if maxel in matrix[i]:
    maxel_inx = i

matrix[minel_inx], matrix[maxel_inx] = matrix[maxel_inx], matrix[minel_inx]

print(matrix)
