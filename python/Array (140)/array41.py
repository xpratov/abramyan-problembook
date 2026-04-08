n = int(input("N - butun sonini kiriting: "))
numbers = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

most = numbers[0] + numbers[1]
add1, add2 = numbers[0], numbers[1]

for i in range(len(numbers)-1):
  if numbers[i] + numbers[i+1] > most:
    most = numbers[i] + numbers[i+1]
    add1, add2 = numbers[i], numbers[i+1]

print(add1, add2)
