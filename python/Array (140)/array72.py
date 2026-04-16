n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k, l = map(int, input("K va L butun sonlarini kiriting: ").split())

start = k - 1
end = l - 1

for i in range((end - start + 1) // 2):
    a[start + i], a[end - i] = a[end - i], a[start + i]

print(a)