n = int(input("N ni kiriting: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

broken_index = 0  

for i in range(n-1):
  if (a[i]>0 and a[i+1]>0) or (a[i]<0 and a[i+1]<0):
    broken_index = i+2
    break

print(broken_index)
