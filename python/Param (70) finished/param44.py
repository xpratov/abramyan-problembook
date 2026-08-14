def DecToBin(N):
    if N == 0:
        return "0"

    res = ""

    while N > 0:
        res = str(N % 2) + res
        N //= 2

    return res


for _ in range(5):
    n = int(input())
    print(DecToBin(n))