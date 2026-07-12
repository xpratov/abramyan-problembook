N = int(input())

kopaytma = 1.0

for _ in range(N):
    son = float(input())
    
    kasr_qism = son - int(son)
    
    print(kasr_qism)
    
    kopaytma *= kasr_qism
print("Ko'paytma:", kopaytma)