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

length = 1
current = P1

while current.Next is not None:
  current = current.Next
  length +=1

P3 = P1
for i in range(length//2-1):
  P3 = P3.Next
  
P4 = P3.Next

P3.Next = P1
P1.Prev = P3

P4.Prev = current
current.Next = P4

print(P3, P4)
