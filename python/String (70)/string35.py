s = input("S - Satrni kiriting: ")
s0 = input("S0 - Qism satrni kiriting: ")

count = s.count(s0)
s = s.replace(s0, "", count)
print(s)
