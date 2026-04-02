v1, v2, s, t = map(int, input("mashina1, mashina2, masofa, vaqt qiymatlarini kiriting: ").split())

result = abs(s-t*(v1+v2))

print("Mashinalar orasida masofa: ", result)