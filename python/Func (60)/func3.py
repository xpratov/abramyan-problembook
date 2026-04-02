pi = 3.14
a, b, c = map(int, input("3 ta aylananing radiuslarini kiriting: ").split())

def circleS(r):
  return f"Radiusi {r}ga teng bo'lgan aylananing yuzi: {(int((pi*r*r)*100))/100}"

print(circleS(a))
print(circleS(b))
print(circleS(c))
