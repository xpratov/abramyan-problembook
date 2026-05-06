n = int(input("N - butun sonini kiriting: "))
array = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k, l = map(int, input("K va L sonlarini kiriting: ").split())

diff = abs(k-l)+1

for i in range(diff):
  array.pop(k-1)

print(len(array), array)