K = int(input())

tartib_raqam = 0
orun = 0
topildi = False

while True:
    son = int(input())
    if son == 0:
        break
    
    orun += 1
    
    if son > K and not topildi:
        tartib_raqam = orun
        topildi = True

print(tartib_raqam)