M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)
    
transposed = [list(col) for col in zip(*matrix)]

transposed.sort(key=lambda x: x[-1], reverse=True)

result = [list(row) for row in zip(*transposed)]

print(matrix)