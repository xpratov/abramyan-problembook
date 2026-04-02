n = int(input("N butun sonini kiriting: "))
nums = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

mx=max(nums)

first = "notfound"
last = 0

for i in range(len(nums)):
  if first=="notfound":
    if nums[i]==mx:
      first = i+1
  else: 
    if nums[i]==mx:
      last = i+1

print(first, last)
  