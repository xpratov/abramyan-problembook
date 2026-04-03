n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta 0 va 1 son kiriting: ").split()))

if n == 0:
    print(0, 0)
else:
    longest = 1
    count = 1
    start_pos = 1
    
    current_start = 1

    for i in range(1, n):
        if numbers[i] == numbers[i-1]:
            count += 1
        else:
            if count > longest:
                longest = count
                start_pos = current_start
            count = 1
            current_start = i + 1

    if count > longest:
        longest = count
        start_pos = current_start

    print(start_pos, longest)