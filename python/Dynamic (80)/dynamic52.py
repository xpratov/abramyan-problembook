class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


# 1-ro'yxat
P1 = Node(10)
P1.Next = Node(20)
P1.Next.Prev = P1
P1.Next.Next = Node(30)
P1.Next.Next.Prev = P1.Next

P2 = P1.Next.Next


# 2-ro'yxat
head = Node(1)
head.Next = Node(2)
head.Next.Prev = head
head.Next.Next = Node(3)
head.Next.Next.Prev = head.Next
head.Next.Next.Next = Node(4)
head.Next.Next.Next.Prev = head.Next.Next

P0 = head.Next 

next_node = None

if P0.Next is not None:
  next_node = P0.Next
  P0.Next = P1
  P1.Prev = P0

if next_node is not None:
  P2.Next = next_node
  next_node.Prev = P2

P1_new = P0
P2_new = P0

while P1_new.Prev is not None:
  P1_new = P1_new.Prev

while P2_new.Next is not None:
  P2_new = P2_new.Next

print(P1_new.Data)
print(P2_new.Data)

