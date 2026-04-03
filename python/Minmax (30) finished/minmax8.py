n = int(input("N - butun sonlar sonini kiriting: "))
nums = list(map(int, input(f"{n} ta butun sonlar kiriting: ").split()))

first_min_inx = 0
last_min_inx = 0

for i in range(n):
  if nums[first_min_inx]>nums[i]:
    first_min_inx=i
  if nums[last_min_inx]>=nums[i]:
    last_min_inx=i

print(first_min_inx+1, last_min_inx+1)