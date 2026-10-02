class TNode:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


if P0.Prev is not None:
    P0.Prev.Next = P0.Next
else:
    P1 = P0.Next

P0.Next.Prev = P0.Prev


P = P0.Prev

for i in range(K - 1):
    if P.Prev is None:
        break
    P = P.Prev


P0.Prev = P.Prev
P0.Next = P

if P.Prev is not None:
    P.Prev.Next = P0
else:
    P1 = P0

P.Prev = P0


PFirst = P1
PLast = P1

while PLast.Next is not None:
    PLast = PLast.Next

print(id(PFirst))
print(id(PLast))