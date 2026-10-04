class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


# Ro'yxat
head = Node(10)
head.Next = Node(20)
head.Next.Prev = head
head.Next.Next = Node(30)
head.Next.Next.Prev = head.Next
head.Next.Next.Next = Node(40)
head.Next.Next.Next.Prev = head.Next.Next
head.Next.Next.Next.Next = Node(50)
head.Next.Next.Next.Next.Prev = head.Next.Next.Next
head.Next.Next.Next.Next.Next = Node(60)
head.Next.Next.Next.Next.Next.Prev = head.Next.Next.Next.Next


# PX va PY
PX = head.Next                  # 20
PY = head.Next.Next.Next.Next   # 50

if PX.Next != PY:
  start = PX.Next
  end = PY.Prev

  start.Prev = None
  end.Next = None

  PX.Next = PY
  PY.Prev = PX
  print(id(start))
else:
  print(None)
print(id(head))
