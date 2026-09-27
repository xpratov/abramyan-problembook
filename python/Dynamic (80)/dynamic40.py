class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


P1 = Node(10)
P2 = Node(21)
P3 = Node(30)
P4 = Node(41)
P5 = Node(50)

P1.next = P2
P2.prev = P1
P2.next = P3
P3.prev = P2
P3.next = P4
P4.prev = P3
P4.next = P5
P5.prev = P4


current = P1
last = P1

while current is not None:
    if current.data % 2 != 0:
        new_node = Node(current.data)

        new_node.prev = current
        new_node.next = current.next

        if current.next is not None:
            current.next.prev = new_node
        else:
            last = new_node

        current.next = new_node
        last = new_node

        current = new_node.next
    else:
        current = current.next


print(id(last))