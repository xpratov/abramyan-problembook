n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

for i in range(0, n-k):
  array[i] = array[i+k]
for i in range(n-k, n):
  array[i] = 0

print(array)