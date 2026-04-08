n = int(input("N - butun sonini kiriting: "))
integers = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

unicals = list(set(integers))
howmany = []

for i in unicals:
  howmany.append(integers.count(i))

print(max(howmany))