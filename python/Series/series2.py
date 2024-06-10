nums = list(map(float, input("10 ta haqiqiy son kiriting: ").split()))

product = 1
for i in nums:
  product*=i

print("Ko'paytma: ", product)