s = input("S - Satrni kiriting: ")
s0 = input("S0 - Qism satrni kiriting: ")

idx = s.rfind(s0)

if idx != -1:
    s = s[:idx] + s[idx + len(s0):]

print("Natija:", s)