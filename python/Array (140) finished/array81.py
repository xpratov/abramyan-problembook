n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

for i in range(n - 1, k - 1, -1):
    array[i] = array[i - k]

for i in range(k):
    array[i] = 0

print(array)