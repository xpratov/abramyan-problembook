s1 = input("Haqiqiy sonlar fayli: ")
s2 = input("Natija fayli: ")

with open(s1, "r") as f:
    a = list(map(float, f.read().split()))

with open(s2, "w") as f:
    i = 0

    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            cnt = 2
            i += 1

            while i < len(a) - 1 and a[i] > a[i + 1]:
                cnt += 1
                i += 1

            f.write(str(cnt) + " ")
        else:
            i += 1