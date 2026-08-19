class Node: 
  def __init__(self, data, next=None):
    self.Data = data
    self.Next = next

P1= Node(40)
P1.Next = Node(30)
P1.Next.Next = Node(20)
P1.Next.Next.Next = Node(10)

D = 50

P2 = Node(D)
P2.Next = P1
P1 = P2

