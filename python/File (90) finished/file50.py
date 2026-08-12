s1 = input("1-fayl: ")
s2 = input("2-fayl: ")
s3 = input("Yangi fayl: ")

with open(s1) as f:
    A = list(map(float, f.read().split()))

with open(s2) as f:
    B = list(map(float, f.read().split()))

i = 0
j = 0
result = []

while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        result.append(str(A[i]))
        i += 1
    else:
        result.append(str(B[j]))
        j += 1

while i < len(A):
    result.append(str(A[i]))
    i += 1

while j < len(B):
    result.append(str(B[j]))
    j += 1

with open(s3, "w") as f:
    f.write(" ".join(result))