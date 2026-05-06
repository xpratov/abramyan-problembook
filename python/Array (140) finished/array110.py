n = int(input("N: "))
numbers = list(map(float, input().split()))

for i in range(len(numbers)-1, -1, -1):
  if numbers[i]%2==0:
    numbers.insert(i+1, numbers[i])

print(numbers)