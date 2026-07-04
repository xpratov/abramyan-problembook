B = float(input())
N = int(input())

b_chiqdi = False

for _ in range(N):
    son = float(input())
    
    if not b_chiqdi and B < son:
        print(B)
        b_chiqdi = True
        
    print(son)

if not b_chiqdi:
    print(B)