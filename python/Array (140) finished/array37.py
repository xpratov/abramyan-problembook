n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

if n == 0:
    print(0)
else:
    count = 1 
    
    for i in range(1, n):
        if a[i] < a[i-1]:
            count += 1

    print("O'suvchi qismlar soni:", count)