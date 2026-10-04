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
P1.Next.Next.Next.Next = Node(50)
P1.Next.Next.Next.Next.Prev = P1.Next.Next.Next
P1.Next.Next.Next.Next.Next = Node(60)
P1.Next.Next.Next.Next.Next.Prev = P1.Next.Next.Next.Next

P2 = P1.Next.Next.Next.Next.Next

K = 2

P1.Prev = P2
P2.Next = P1

new_first = P1
for i in range(K):
    new_first = new_first.Next

new_last = new_first.Prev

new_first.Prev = None
new_last.Next = None

P1 = new_first
P2 = new_last

print(P1.Data)
print(P2.Data)