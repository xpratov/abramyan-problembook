n = int(input("N = "))

f_prev, f_curr = 1, 1
while f_curr < n:
    f_prev, f_curr = f_curr, f_prev + f_curr

print(f"Oldingisi: {f_prev}, Keyingisi: {f_prev + f_curr}")