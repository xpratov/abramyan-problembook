s1 = input("1-fayl: ")
s2 = input("2-fayl: ")

with open(s1, "rb") as f:
    data1 = f.read()

with open(s2, "rb") as f:
    data2 = f.read()

with open(s1, "ab") as f:
    f.write(data2)

with open(s2, "ab") as f:
    f.write(data1)