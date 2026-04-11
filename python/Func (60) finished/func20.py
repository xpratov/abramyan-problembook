nums = list(map(int, input("5 ta son kiriting: ").split()))

def fact2(n):
  result = 1
  if n%2==1:
    for i in range(1, n+1, 2):
      result*=i
  else:
    for i in range(2, n+1, 2):
      result*=i
  return result

for i in nums:
  print(f"{i} ning dubl-faktoriali {fact2(i)} ga teng.")
