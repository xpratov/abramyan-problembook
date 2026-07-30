sa = input("A fayl: ")
sb = input("B fayl: ")
sc = input("C fayl: ")
sd = input("D fayl: ")
se = input("Yangi fayl: ")

with open(sa) as f:
    A = f.read().split()

with open(sb) as f:
    B = f.read().split()

with open(sc) as f:
    C = f.read().split()

with open(sd) as f:
    D = f.read().split()

n = min(len(A), len(B), len(C), len(D))

result = []

for i in range(n):
    result.extend([A[i], B[i], C[i], D[i]])

with open(se, "w") as f:
    f.write(" ".join(result))