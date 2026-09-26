class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TQueue:
    def __init__(self, head=None, tail=None):
        self.Head = head
        self.Tail = tail


def Dequeue(Q):
    value = Q.Head.data

    old_head = Q.Head
    Q.Head = Q.Head.next

    if Q.Head is None:
        Q.Tail = None

    del old_head

    return value


N = int(input())
numbers = list(map(int, input().split()))

Q = TQueue()

for value in numbers:
    new_node = Node(value)

    if Q.Head is None:
        Q.Head = new_node
        Q.Tail = new_node
    else:
        Q.Tail.next = new_node
        Q.Tail = new_node


for _ in range(5):
    print(Dequeue(Q))


if Q.Head is None:
    print("nil")
    print("nil")
else:
    print(id(Q.Head))
    print(id(Q.Tail))