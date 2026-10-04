class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


# Birinchi ro'yxat
P1 = Node(10)
P1.Next = Node(20)
P1.Next.Prev = P1
P1.Next.Next = Node(30)
P1.Next.Next.Prev = P1.Next

P2 = P1.Next.Next


# Ikkinchi ro'yxat
Q1 = Node(40)
Q1.Next = Node(50)
Q1.Next.Prev = Q1
Q1.Next.Next = Node(60)
Q1.Next.Next.Prev = Q1.Next

P0 = Q1.Next

after_node = P0.Next

P0.Next = P1
P1.Prev = P0

P2.Next = after_node
after_node.Prev = P2

last_node = after_node
while last_node.Next is not None:
  last_node = last_node.Next

print(Q1, last_node)