class Node:
  def __init__(self, data, next=None):
    self.Data = data
    self.Next = next

P1 = Node(10)
P1.Next = Node(20)
P1.Next.Next = Node(30)

p = P1

while p is not None:
  print(p.Data)
  p = p.Next

P2 = P1.Next

print(P2.Data)
