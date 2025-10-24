x1, y1=map(int, input("x1 va y1: ").split())
x2, y2=map(int, input("x1 va y1: ").split())

a=abs(x1-x2)
b=abs(y1-y2)

print(f"Perimetri: {2*(a+b)}")
print(f"Yuzasi: {a*b}")
