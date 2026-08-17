filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

count = 0
inside = False

for line in lines:
    if line.strip() != "":
        if not inside:
            count += 1
            inside = True
    else:
        inside = False

print(count)