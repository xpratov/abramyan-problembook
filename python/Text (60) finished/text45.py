with open("input.txt", "r") as f:
    count = 0
    total = 0

    for line in f:
        x = float(line.strip())

        if not x.is_integer():
            count += 1
            total += x

print("Amount:", count)
print("Sum:", total)