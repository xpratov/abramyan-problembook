class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


P1 = Node(10)
P2 = Node(20)
P3 = Node(30)

P1.next = P2
P2.prev = P1
P2.next = P3
P3.prev = P2

position = 1
current = P1

while current is not None:
    next_node = current.next

    if position % 2 == 1:
        if current.prev is not None:
            current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev

        if current == P1:
            P1 = current.next

        del current

    position += 1
    current = next_node

print(P1)