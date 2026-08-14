def PosK(S0, S, K):
    start = 0
    count = 0

    while True:
        pos = S.find(S0, start)

        if pos == -1:
            return 0

        count += 1

        if count == K:
            return pos + 1

        start = pos + len(S0)


for i in range(5):
    S0 = input()
    S = input()
    K = int(input())

    print(PosK(S0, S, K))