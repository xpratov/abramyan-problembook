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


before = PX.Prev
after = PY.Next


new_head = PX
new_head.Prev = None

new_tail = PY
new_tail.Next = None


if before is not None:
    before.Next = after

if after is not None:
    after.Prev = before


if before is not None:
    head1 = head
else:
    head1 = after


print(id(head1) if head1 is not None else None)
print(id(new_head))