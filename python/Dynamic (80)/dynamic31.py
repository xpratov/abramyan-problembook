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

# P0 berilgan deb tasavvur qilamiz
P0 = P4

first = P0

while first.prev is not None:
  first = first.prev

last = P0

while last.next is not None:
  last = last.next

N = 0
current = first

while current.next is not None:
  N += 1
  current = current.next

print(N)
print(id(first))
print(id(last))