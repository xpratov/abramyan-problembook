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


P0 = P3

if P0 != P1:

    P0.prev.next = P0.next

    if P0.next is not None:
        P0.next.prev = P0.prev

    P0.prev = None
    P0.next = P1
    P1.prev = P0

    P1 = P0

last = P1

while last.next is not None:
    last = last.next

print(P1)
print(last)