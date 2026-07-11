count = 0

def Combin1(n, k):
    global count
    count += 1

    if k == 0 or k == n:
        return 1

    return Combin1(n - 1, k) + Combin1(n - 1, k - 1)


n = int(input("N ni kiriting: "))
klar = list(map(int, input("5 ta K ni kiriting: ").split()))

for k in klar:
    count = 0
    result = Combin1(n, k)
    print(f"C({n}, {k}) = {result}, Rekursiv chaqiriqlar soni = {count}")