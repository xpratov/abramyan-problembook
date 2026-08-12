I = int(input())
J = int(input())

with open("input.txt", "r") as f:
    data = list(map(float, f.read().split()))

m = int(data[0])       # ustunlar soni
a = data[1:]           # matritsa elementlari

if J > m or J < 1:
    print(0.0)
else:
    elements = len(a)

    if elements % m != 0:
        print(0.0)
    else:
        n = elements // m

        if I < 1 or I > n:
            print(0.0)
        else:
            index = (I - 1) * m + (J - 1)
            print(a[index])