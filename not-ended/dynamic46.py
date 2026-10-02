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


P = P0.Next

for i in range(K):
    if P.Next is None:
        break
    P = P.Next


P0.Prev = P
P0.Next = P.Next

if P.Next is not None:
    P.Next.Prev = P0

P.Next = P0


PFirst = P1
PLast = P1

while PLast.Next is not None:
    PLast = PLast.Next

print(id(PFirst))
print(id(PLast))