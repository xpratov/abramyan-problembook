n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

left = 0      
right = n - 1 

while left <= right:
    for _ in range(2):
        if left <= right:
            print(a[left])
            left += 1

    for _ in range(2):
        if left <= right:
            print(a[right])
            right -= 1