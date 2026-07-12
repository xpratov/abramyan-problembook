N = int(input())

oldingi_son = None

for _ in range(N):
    son = int(input())
    
    if son != oldingi_son:
        print(son)
        oldingi_son = son