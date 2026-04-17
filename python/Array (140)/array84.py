n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

array.append(array.pop(0))

print(array)