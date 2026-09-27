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

# P1 — birinchi, P2 — oxirgi komponent deb tasavvur qilamiz
P1 = P1
P2 = P4


new_first = Node(P1.data)

new_first.next = P1
P1.prev = new_first


new_last = Node(P2.data)

new_last.prev = P2.prev
new_last.next = P2

P2.prev.next = new_last
P2.prev = new_last


print(id(new_first))