n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

array.insert(0, array.pop())

print(array)