
def AddRightDigit(D, K):
    return K * 10 + D

K = int(input("K sonini kiriting: "))
D1 = int(input("D1 raqamini kiriting: "))
D2 = int(input("D2 raqamini kiriting: "))

K = AddRightDigit(D1, K)
print(f"D1 qo'shilgandan keyin: {K}")

K = AddRightDigit(D2, K)
print(f"D2 qo'shilgandan keyin: {K}")