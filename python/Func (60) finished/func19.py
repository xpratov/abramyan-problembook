nums = list(map(int, input("5 ta butun son kiriting: ").split()))

def fact(n):
  result = 1
  for i in range(n):
    result*=(i+1)
  return result

for i in nums:
  print(f"{i} ning faktoriali {fact(i)} ga teng.")