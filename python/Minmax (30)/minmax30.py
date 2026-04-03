n = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mx = max(numbers)

count = 0
little = n 

for i in numbers:
    if i == mx:
        count += 1
    else:
        if count > 0:
            if count < little:
                little = count
        count = 0

if count > 0 and count < little:
    little = count

print(little)