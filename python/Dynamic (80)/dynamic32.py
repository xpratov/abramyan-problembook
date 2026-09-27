class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

P1 = Node(10)
P2 = Node(20)
P3 = Node(30)
P4 = Node(40)
P5 = Node(50)

P1.next = P2

P2.prev = P1
P2.next = P3

P3.prev = P2
P3.next = P4

P4.prev = P3
P4.next = P5

P5.prev = P4

D1 = 5
D2 = 55

# P0 berilgan deb tasavvur qilamiz
P0 = P3

new_first = Node(D1)

new_first.next = P1
P1.prev = new_first
P1 = new_first

new_last  = Node(D2)
P5.next = new_last
new_first.prev = P5
P5 = new_last

print(id(new_first))
print(id(new_last))
