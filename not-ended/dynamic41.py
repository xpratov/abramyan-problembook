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

# P0 berilgan 
P0 = P3

prev = P0.prev
next = P0.next

if prev is not None:
    prev.next = next

if next is not None:
    next.prev = prev

print(prev)
print(next)

del P0