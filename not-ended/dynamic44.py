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

P0 = P2

if P0.next is not None:

    if P0.prev is not None:
        P0.prev.next = P0.next

    P0.next.prev = P0.prev

    last = P0.next

    while last.next is not None:
        last = last.next

    last.next = P0
    P0.prev = last
    P0.next = None

    if P0 == P1:
        P1 = P0.prev

print(P1)
print(P0)