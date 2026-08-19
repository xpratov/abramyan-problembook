class Node:
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next


P1 = Node(5)
P1.Next = Node(7)
P1.Next.Next = Node(8)
P1.Next.Next.Next = Node(11)

P2 = Node(20)
P2.Next = Node(30)


while P1 is not None and P1.Data % 2 != 0:
    temp = P1.Next

    P1.Next = P2
    P2 = P1

    P1 = temp


print("P1:", P1.Data if P1 is not None else None)
print("P2:", P2.Data if P2 is not None else None)