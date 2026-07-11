def Combin2(n, k, memo):
    if memo[n][k] != -1:
        return memo[n][k]

    if k == 0 or k == n:
        memo[n][k] = 1
    else:
        memo[n][k] = Combin2(n - 1, k, memo) + Combin2(n - 1, k - 1, memo)

    return memo[n][k]


n = int(input("N ni kiriting: "))
klar = list(map(int, input("5 ta K ni kiriting: ").split()))

# N <= 20
memo = [[-1] * 21 for _ in range(21)]

for k in klar:
    print(Combin2(n, k, memo))