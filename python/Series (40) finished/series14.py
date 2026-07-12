K = int(input())

soni = 0

while True:
    son = int(input())
    if son == 0:
        break
    if son < K:
        soni += 1

print(soni)