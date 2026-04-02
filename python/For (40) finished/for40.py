a, b = map(int, input("A, B - butun sonlarni kiriting: ").split())

time = 1

for i in range(a, b+1):
  for j in range(time):
    print(i)
  time+=1

