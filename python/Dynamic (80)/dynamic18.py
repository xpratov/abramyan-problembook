class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

D = int(input("D - butun sonini kiriting: "))
values = list(map(int, input("Queue'ning qiymatlarini kiriting: ").split()))

head = tail = None

for value in values:
  new_node = Node(value)
  if head is None:
    head = tail = new_node
  else:
    tail.next = new_node
    tail = new_node

DNode = Node(D)
tail.next = DNode
tail = DNode

head_node = head
head = head.next
print(head_node.data)

print(head, tail)

head_node = None


