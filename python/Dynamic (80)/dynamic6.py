class Node:
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next


P1 = Node(90)
P1.Next = Node(80)
P1.Next.Next = Node(70)
P1.Next.Next.Next = Node(60)
P1.Next.Next.Next.Next = Node(50)
P1.Next.Next.Next.Next.Next = Node(40)
P1.Next.Next.Next.Next.Next.Next = Node(30)
P1.Next.Next.Next.Next.Next.Next.Next = Node(20)
P1.Next.Next.Next.Next.Next.Next.Next.Next = Node(10)
P1.Next.Next.Next.Next.Next.Next.Next.Next.Next = Node(5)


for _ in range(9):
    print(P1.Data)

    old = P1
    P1 = P1.Next

    old = None


P2 = P1

print("P2.Data =", P2.Data)