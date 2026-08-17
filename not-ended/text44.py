with open("input.txt", "r") as f:
    count = 0
    total = 0

    for line in f:
        n = int(line.strip())

        count += 1
        total += n

print("Amount:", count)
print("Sum:", total)