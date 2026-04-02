x1, y1 = map(int, input("Shaxmat doskasidagi katak1'ning kordinatasini kiriting: ").split())
x2, y2 = map(int, input("Shaxmat doskasidagi katak2'ning kordinatasini kiriting: ").split())

def isWhite(x, y):
  if x%2==0 and y%2==1 or x%2==1 and y%2==0:
    return True
  return False

print(f"{x1, y1} katak bilan {x2, y2} kataklarning ranglari bir xil?")
if isWhite(x1, y1) == isWhite(x2, y2):
  print(True)
else:
  print(False)
