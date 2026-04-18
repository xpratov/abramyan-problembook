n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

write = 0 

for i in range(n):
  if array[i]%2==0:
    array[write] = array[i]
    write+=1

del array[write:]

print(len(array), array)