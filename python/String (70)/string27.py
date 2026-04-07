n1, n2 = map(int, input("N1 va N2 butun sonlarini kiriting: ").split())

s1 = input("S1 satrini kiriting: ")
s2 = input("S2 satrini kiriting: ")

if n2 == 0:
    result = s1[:n1]
else:
    result = s1[:n1] + s2[-n2:]

print("Natija:", result)