def DecToHex(N):
    if N == 0:
        return "0"

    digits = "0123456789ABCDEF"
    res = ""

    while N > 0:
        res = digits[N % 16] + res
        N //= 16

    return res


for _ in range(5):
    n = int(input())
    print(DecToHex(n))