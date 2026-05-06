n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

for i in range(n // 2):
    print(a[i])         
    print(a[n - 1 - i]) 

if n % 2 != 0:
    print(a[n // 2])