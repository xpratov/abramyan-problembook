n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k, l = map(int, input("K va L butun sonlarini kiriting: ").split())

a[k:l-1] = a[k:l-1][::-1]

print(a)