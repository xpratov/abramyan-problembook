M = int(input("M (satrlar): "))
N = int(input("N (ustunlar): "))

matrix = []
for i in range(M):
    matrix.append(list(map(int, input().split())))

k1, k2 = map(int, input("K1 va K2 - butun sonlarni kiriting: ").split())

matrix[k1-1], matrix[k2-1] = matrix[k2-1], matrix[k1-1]

print(matrix)