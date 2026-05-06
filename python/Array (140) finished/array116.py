n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

b = [] 
c = [] 

if n > 0:
    current_val = a[0]
    count = 1
    
    for i in range(1, n):
        if a[i] == current_val:
            count += 1
        else:
            b.append(count)
            c.append(current_val)
            current_val = a[i]
            count = 1
            
    b.append(count)
    c.append(current_val)

print("B (uzunliklar):", *b)
print("C (qiymatlar):", *c)