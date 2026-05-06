a = list(map(int, input("10 ta butun son kiriting: ").split()))

first_element = a[0]
last_element = a[9]

result_order = 0

for i in range(8, 0, -1):
    if first_element < a[i] < last_element:
        result_order = i + 1 
        break

print(result_order)