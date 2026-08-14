def WordK(S, K):
    words = S.split()

    if K > len(words):
        return ""

    return words[K - 1]


S = input()

for i in range(3):
    K = int(input())
    print(WordK(S, K))