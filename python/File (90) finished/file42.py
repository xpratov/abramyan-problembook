s1 = input("1-fayl nomi: ")
s2 = input("2-fayl nomi: ")

with open(s1, "rb") as f:
    data1 = f.read()

with open(s2, "rb") as f:
    data2 = f.read()

with open(s1, "wb") as f:
    f.write(data2)

with open(s2, "wb") as f:
    f.write(data1)