N = int(input())

yigindi = 0

for _ in range(N):
    son = float(input())
    
    yaxlitlangan = round(son)
    
    print(yaxlitlangan)
    
    yigindi += yaxlitlangan

print("Yig'indi:", yigindi)