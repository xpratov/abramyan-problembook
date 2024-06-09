from math import sqrt
print("Uchburchakning 3 ta uchlari kordinata o'qidagi nuqtalari kiritiladi. Uning yuzini geron formulasi yordamida topilsin.")
x1, y1=map(int, input("x1 va y1'larni kiriting: ").split())  # A
x2, y2=map(int, input("x2 va y2'larni kiriting: ").split())  # B
x3, y3=map(int, input("x3 va y3'larni kiriting: ").split())  # C

def pifagor(katet1, katet2):
  return int(sqrt(katet1**2+katet2**2))

AB = pifagor(abs(x1-x2), abs(y1-y2))
BC = pifagor(abs(x2-x3), abs(y2-y3))
CA = pifagor(abs(x3-x1), abs(y3-y1))

p=(AB+BC+CA)/2

S=sqrt(p*(p-AB)*(p-BC)*(p-CA))

print(f"Yuza: {S:.3}")