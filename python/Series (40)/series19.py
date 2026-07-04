N = int(input())

K = 0
oldingi_son = int(input())

for _ in range(N - 1):
    son = int(input())
    
    if son < oldingi_son:
        print(son)
        K += 1
        
    oldingi_son = son

print("K =", K)