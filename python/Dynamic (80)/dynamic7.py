class Node:
  def __init__(self, data, next=None):
    self.Data = data
    self.Next = next

P1 = Node(10)
P1.Next = Node(20)
P1.Next.Next = Node(30)
P1.Next.Next.Next = Node(40)

count = 0
while P1 is not None:
  print(P1.Data)
  P1 = P1.Next
  count += 1

print(count)

