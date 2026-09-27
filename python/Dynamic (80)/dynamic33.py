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


D = 55
P0 = P3

new_node = Node(D)

new_node.prev = P0.prev
new_node.next = P0

P0.prev.next = new_node
P0.prev = new_node

print(id(new_node))