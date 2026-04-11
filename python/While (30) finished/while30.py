a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

count_a = 0
temp_a = a
while temp_a >= c:
    temp_a -= c
    count_a += 1

count_b = 0
temp_b = b
while temp_b >= c:
    temp_b -= c
    count_b += 1

total_squares = 0
for _ in range(count_b):
    total_squares += count_a

print("Jami kvadratlar soni:", total_squares)