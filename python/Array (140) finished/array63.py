a = list(map(float, input("A massivi uchun 5 ta son kiriting: ").split()))
b = list(map(float, input("B massivi uchun 5 ta son kiriting: ").split()))

c = [0] * 10  
i = 0  
j = 0  
k = 0  

while i < 5 and j < 5:
    if a[i] < b[j]:
        c[k] = a[i]
        i += 1
    else:
        c[k] = b[j]
        j += 1
    k += 1

while i < 5:
    c[k] = a[i]
    i += 1
    k += 1

while j < 5:
    c[k] = b[j]
    j += 1
    k += 1

print("Natijaviy C massivi:")
print(c)