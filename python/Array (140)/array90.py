n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

array.pop(k-1)

print(array)