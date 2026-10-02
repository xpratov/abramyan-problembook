class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


P1 = Node(10)
P2 = Node(20)
P3 = Node(30)
P4 = Node(40)

P1.next = P2

P2.prev = P1
P2.next = P3

P3.prev = P2
P3.next = P4

P4.prev = P3

PX = P2
PY = P4


PX_prev = PX.prev
PX_next = PX.next

PY_prev = PY.prev
PY_next = PY.next


if PX_prev:
    PX_prev.next = PY

PY.prev = PX_prev

if PX_next:
    PX_next.prev = PY

PY.next = PX_next


if PY_prev:
    PY_prev.next = PX

PX.prev = PY_prev

if PY_next:
    PY_next.prev = PX

PX.next = PY_next


P = PX

while P.prev is not None:
    P = P.prev


while P is not None:
    print(P.data, end=" ")
    P = P.next