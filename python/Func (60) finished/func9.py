nums = list(map(int, input("10 ta son kiriting: ").split()))

def even(k):
  if k%2==0:
    return True
  return False

evens = [i for i in nums if even(i)]

print(sum(evens))