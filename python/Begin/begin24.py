a, b, c = map(int, input("A, B, C sonlarini kiriting: ").split())

a, b, c = c, a, b
print(f"A Cga, C Bga, B Aga o'zgartirildi!\nA = {a}\nB = {b}\nC = {c}")