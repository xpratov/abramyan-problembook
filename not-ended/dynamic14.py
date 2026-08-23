class TNode:
  def __init__(self, data):
    self.data = data
    self.next = None

values = list(map(int, input("10 ta butun son kiriting: ").split()))

head = None
tail = None

for value in values:
  new_node = TNode(value)
  if head is None:
    head = new_node
    tail = new_node
  else:
    tail.next = new_node
    tail = new_node

print(head, tail)