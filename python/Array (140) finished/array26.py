n = int(input("N ni kiriting: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

broken_index = 0  

for i in range(n-1):
  if a[i]%2 == a[i+1]%2:
    broken_index = i=2
    break

print(broken_index)
