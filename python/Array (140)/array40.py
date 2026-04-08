r = float(input("R - haqiqiy sonini kiriting: "))
n = int(input("N - butun sonini kiriting: "))
floats = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

result = floats[0] 

for i in floats:
    if abs(i - r) < abs(result - r):
        result = i

print(result)