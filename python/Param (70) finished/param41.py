def SplitStr(S):
    W = S.split()
    N = len(W)
    return W, N


S = input("S = ")

W, N = SplitStr(S)

print(N)

for word in W:
    print(word)