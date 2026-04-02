nums = list(map(int, input("5 ta son kiriting: ").split()))


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

for i in nums:
    print(f"{i} sonining faktoriali: {fact(i)}")