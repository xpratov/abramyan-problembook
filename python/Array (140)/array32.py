n = int(input("N - butun sonini kiriting: "))
floats = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

if n > 1 and floats[0] < floats[1]:
    print(1)
elif n == 1:
    print(1)
else:
    found = False
    for i in range(1, len(floats)-1):
        if floats[i-1] > floats[i] < floats[i+1]:
            print(i+1)
            found = True
            break

    if not found and n > 1 and floats[-1] < floats[-2]:
        print(n)