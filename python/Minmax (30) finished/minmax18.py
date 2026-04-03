n = int(input("N: "))
numbers = list(map(int, input().split()))

mx = max(numbers)

total_count = 0 
temp_count = 0  
found_any = False

for i in numbers:
    if i == mx:
        if found_any:
            total_count += temp_count + 1 
        found_any = True
        temp_count = 0 
    else:
        if found_any:
            temp_count += 1

if total_count > 0:
    print(total_count - 1)
else:
    print(0)