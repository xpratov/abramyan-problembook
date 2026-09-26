class Node:
  def __init__(self, data):
    self.Data = data
    self.Prev = None
    self.Next = None

P1 = Node(10)
P2 = Node(20)
P3 = Node(30)

P1.Next = P2
P2.Prev = P1
P2.Next = P3
P3.Prev = P2

# P2 berilgan deb hisoblaymiz
print(P2.Prev.Data)
print(P2.Next.Data)

print(id(P2.Prev))
print(id(P2.Next))