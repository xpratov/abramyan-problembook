class Node:
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next

P1 = Node(40)
P1.Next = Node(30)
P1.Next.Next = Node(20)
P1.Next.Next.Next = Node(10)

D = P1.Data

P2 = P1.Next

P1 = None

print("D =", D)
print("P2.Data =", P2.Data if P2 is not None else None)