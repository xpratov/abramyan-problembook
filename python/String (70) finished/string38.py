s = input("S - satrni kiriting: ")
s1 = input("S1 - satrni kiriting: ")
s2 = input("S2 - satrni kiriting: ")

count = s.count(s1)

s = s.replace(s1, s2, count)

print(s)