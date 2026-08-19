class Node:
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next


P1 = Node(10)
P1.Next = Node(20)
P1.Next.Next = Node(30)

P2 = Node(40)
P2.Next = Node(50)


while P1 is not None:
    temp = P1.Next

    P1.Next = P2
    P2 = P1

    P1 = temp


print("New top:", P2.Data)

p = P2
while p is not None:
    print(p.Data)
    p = p.Next