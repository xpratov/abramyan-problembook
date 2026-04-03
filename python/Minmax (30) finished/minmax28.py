n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta 0 va 1 son kiriting: ").split()))

if 1 not in numbers:
    print(0, 0)
else:
    count = 0
    max_count = 0
    start_index = 0
    
    current_start = 0

    for i in range(n):
        if numbers[i] == 1:
            if count == 0:
                current_start = i + 1 
            count += 1
        else:
            if count > max_count:
                max_count = count
                start_index = current_start
            count = 0
            
    if count > max_count:
        max_count = count
        start_index = current_start

    print(start_index, max_count)