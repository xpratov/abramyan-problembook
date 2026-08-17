filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

count = 0

for line in lines:
    if line.strip() != "" and line.startswith("     "):
        count += 1

print(count)