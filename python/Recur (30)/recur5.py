def Fib2(n, memo):
    if memo[n] != 0:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = Fib2(n - 1, memo) + Fib2(n - 2, memo)

    return memo[n]


memo = [0] * 21  # N <= 20

for _ in range(5):
    n = int(input())
    print(Fib2(n, memo))