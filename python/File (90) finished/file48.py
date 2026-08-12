sa = input("A fayl: ")
sb = input("B fayl: ")
sc = input("C fayl: ")
sd = input("Yangi fayl: ")

with open(sa, "r") as f:
    A = f.read().split()

with open(sb, "r") as f:
    B = f.read().split()

with open(sc, "r") as f:
    C = f.read().split()

result = []

for i in range(len(A)):
    result.extend([A[i], B[i], C[i]])

with open(sd, "w") as f:
    f.write(" ".join(result))