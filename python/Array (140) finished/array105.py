n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k, m = map(int, input("K va M - butun sonlarini kiriting: ").split())

for i in range(m):
  numbers.insert(k+i, 0.0)

print(numbers)