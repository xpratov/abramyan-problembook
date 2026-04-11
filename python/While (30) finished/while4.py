n = int(input("N musbat butun sonini kiriting: "))

while n % 3 == 0 and n > 0:
    n = n // 3

if n == 1:
    print(True)
else:
    print(False)