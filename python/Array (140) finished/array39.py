n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    count = 1
    direction = 0 

    for i in range(1, n):
        if a[i] > a[i-1]:
            current_dir = 1
        elif a[i] < a[i-1]:
            current_dir = -1
        else:
            current_dir = 0 

        if direction != 0 and current_dir != 0 and direction != current_dir:
            count += 1
            direction = current_dir
        elif direction == 0:
            direction = current_dir

    print("Monotonlik oraliqlari soni:", count)