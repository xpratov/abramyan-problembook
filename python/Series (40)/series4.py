n=int(input())
ns=list(map(int, input(f"{n} ta haqiqiy son kiriting: ").split()))

summa=0
product=1

for i in range(n):
  summa+=ns[i]
  product*=ns[i]

print("Yig'indi: ", summa)
print("Ko'paytmasi: ", product)
