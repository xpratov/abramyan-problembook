import os

s1 = input("1-fayl nomini yozing: ")
s2 = input("2-fayl nomini yozing: ")

if os.path.exists(s1):
    existing = s1
    new = s2
else:
    existing = s2
    new = s1

with open(existing, "r") as f:
    components = f.read().split()

with open(new, "x") as f:
    f.write(components[-1] + "\n")
    f.write(components[0])