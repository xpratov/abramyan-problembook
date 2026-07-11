def Fact2(N):
    if N == 1 or N == 2:
        return float(N)
    
    return float(N * Fact2(N - 2))

numbers = [5, 6, 7, 8, 9]

print("Qo'sh faktorial natijalari:")
for n in numbers:
    result = Fact2(n)
    print(f"{n}!! = {result}")