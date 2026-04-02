a, b, c = map(int, input("A, B, C sonlarini kiriting: ").split())

a, b, c = b, c, a
print(f"A Bga, B Cga, C Aga o'zgartirildi!\nA = {a}\nB = {b}\nC = {c}")