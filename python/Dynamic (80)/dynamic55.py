class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


# Ro'yxat
P1 = Node(10)
P1.Next = Node(20)
P1.Next.Prev = P1
P1.Next.Next = Node(30)
P1.Next.Next.Prev = P1.Next
P1.Next.Next.Next = Node(40)
P1.Next.Next.Next.Prev = P1.Next.Next

last_node = P1

while last_node.Next is not None:
  last_node = last_node.Next

P1.Prev = last_node
last_node.Next = P1

print(id(last_node))

