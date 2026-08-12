I = int(input())
J = int(input())

with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = (len(a) + 2) // 3

print(n)

if I > n or J > n:
    print(-1.0)

elif abs(I - J) > 1:
    print(0.0)

else:
    index = 0

    # I-qatorgacha bo'lgan qatorlar elementlari
    for row in range(1, I):
        if row == 1 or row == n:
            index += 2
        else:
            index += 3

    # I-qator ichidagi pozitsiya
    if I == 1:
        index += J - 1
    else:
        index += J - I + 1

    print(a[index])