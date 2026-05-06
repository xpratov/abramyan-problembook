a = list(map(int, input("10 ta butun son kiriting: ").split()))

last_element = a[9]
result = 0

for i in range(9):
    if a[i] < last_element:
        result = a[i]
        break

print(result)