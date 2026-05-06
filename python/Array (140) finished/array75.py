n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

maxinx = 0
mininx = 0

for i in range(n):
  if a[i]>a[maxinx]:
    maxinx = i
  if a[i]<a[mininx]:
    mininx = i

start = min(mininx, maxinx)
end = max(mininx, maxinx)

a[start:end+1] = a[start:end+1][::-1]

print(a)