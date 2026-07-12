K = int(input())

tartib_raqam = 0
orun = 0

while True:
    son = int(input())
    if son == 0:
        break
    
    orun += 1
    
    if son > K:
        tartib_raqam = orun

print(tartib_raqam)