K = int(input("K = "))
filename = input("Fayl nomi: ")
new_filename = input("Yangi fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

last_lines = lines[-K:]

with open(new_filename, "w") as f:
    f.writelines(last_lines)