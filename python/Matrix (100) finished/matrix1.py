M = int(input("M (qatorlar soni) ni kiritig: "))
N = int(input("N (ustunlar soni) ni kiritig: "))

matrix = []

for i in range(1, M + 1):
    row = [] 
    for j in range(N):
        row.append(10 * i) 
    matrix.append(row) 

print("\nHosil bo'lgan matritsa:")
for row in matrix:
    print(*row)