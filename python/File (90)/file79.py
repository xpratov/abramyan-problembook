with open("SA", "r") as f:
    data_a = list(map(float, f.read().split()))

with open("SB", "r") as f:
    data_b = list(map(float, f.read().split()))

m = int(data_a[0])       # A ustunlari
k = int(data_b[0])       # B ustunlari

A = data_a[1:]
B = data_b[1:]

n = len(A) // m           # A qatorlari
p = len(B) // k           # B qatorlari

with open("SC", "w") as f:

    # A: n × m
    # B: p × k
    # Ko'paytirish uchun m == p bo'lishi kerak

    if m != p:
        pass

    else:
        # Natija n × k
        f.write(str(k) + "\n")

        for i in range(n):
            for j in range(k):

                s = 0

                for t in range(m):
                    s += A[i * m + t] * B[t * k + j]

                f.write(str(s) + " ")

            f.write("\n")